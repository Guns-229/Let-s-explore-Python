#!/usr/bin/python
##  This program is free software: you can redistribute it and/or modify
##	it under the terms of the GNU General Public License as published by
##	the Free Software Foundation, either version 3 of the License, or
##	(at your option) any later version.
##	This program is distributed in the hope that it will be useful,
##	but WITHOUT ANY WARRANTY; without even the implied warranty of
##	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##	GNU General Public License for more details.
##	You should have received a copy of the GNU General Public License
##	along with this program.  If not, see <http://www.gnu.org/licenses>.
########################################

import os
import sys
import shutil
import errno
from difflib import ndiff, HtmlDiff, unified_diff
import filecmp
from optparse import OptionParser
from ConfigParser import ConfigParser
from multiprocessing.dummy import Pool
import json
import slate
from operator import itemgetter

from img_cmp import img_cmp


__version__ = '0.21 Alpha'
filecount = 0
IMG_TYPE=['.jpg', '.jpeg', '.png', '.bmp', '.ppm', '.gif']


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured
# import cProfile
# def do_cprofile(func):
#     """
#     :rtype : object
#     """
#  
#     def profiled_func(*args, **kwargs):
#         profile = cProfile.Profile()
#         try:
#             profile.enable()
#             result = func(*args, **kwargs)
#             profile.disable()
#             return result
#         finally:
#             profile.print_stats()
#  
#     return profiled_func


def pdf2txt(src, dst):
    with open(src) as f:
        doc = slate.PDF(f)
    with open(dst, 'w+') as f:
        f.write("\n".join(doc))
    

def get_zero_size_common_files(common_files, old_folder, new_folder):
    # returns the list of dict of files with zero size.
    #
    zero_files = []
    try:
        for f in common_files:
            file_name = os.path.join(new_folder, f)
            old_size = os.path.getsize(os.path.join(old_folder, f))
            new_size = os.path.getsize(file_name)
            if not (old_size and new_size):
                zero_files.append({'file': f, "old": old_size, 'new': new_size})
    except:
        pass

    return zero_files


def copy_report_files(src, dst):
    """
    copies the report template files in report folder
    """
    lst_files = ['report.html', 'js/jquery.dataTables.min.js', "js/plugins.js",
                 "js/vendor/bootstrap.min.js", "js/jquery.js", "js/vendor/modernizr-2.6.2.min.js",
                 "css/bootstrap-theme.min.css", "css/jquery.dataTables.min.css", "css/bootstrap.min.css"]

    for file_name in lst_files:
        dst_path = os.path.split(os.path.join(dst, file_name))[0]
        if not (os.path.exists(dst_path)):
            os.makedirs(dst_path)
        shutil.copy2(os.path.join(src, 'report_files', file_name), os.path.join(dst, file_name))


def compare_file(input_data):
    """
    Compares two files and return the result.
    using the modules from
    Differ: ndiff, compare, unified_diff, context_diff
    HtmlDiff: make_file

    diff types used are diff, ndiff, html, htmldetail
    """
    try:
        global filecount
        old_file = ''
        diff = ''
        old_file = input_data[0]
        new_file = input_data[1]
        report_folder = input_data[2]
        diff_type = input_data[3]
        sys.stdout.write("Files Left: {0}   \r".format(filecount))
        filecount -= 1
        sys.stdout.write("{0},\n".format(old_file))
        sys.stdout.flush()
        

        if not filecmp.cmp(old_file, new_file):
            # Ok, we now knows that the files are different 
            # so lets get the file type and extract the texts from it or 
            # in case of images lets 
            diff_file = os.path.join(report_folder, os.path.split(old_file)[1])
            # if its an image then compare using img_cmp and save the extension as whats in 
            # the source files.
            ext = os.path.splitext(input_data[0])[1].lower()
            if ext in IMG_TYPE:
                img_cmp(old_file, new_file, diff_file)
            else:
                if( ext == '.pdf'):
                    old_f = old_file
                    old_file = old_file + '.txt'
                    new_f = new_file
                    new_file= new_file + '.txt'
                    
                    pdf2txt(old_f, old_file)
                    pdf2txt(new_f, new_file)
         
                old_file_data = open(old_file, 'U').readlines()
                new_file_data = open(new_file, 'U').readlines()
                if diff_type == 'ndiff':
                    diff = ndiff(old_file_data, new_file_data)
                    diff_file += '.diff'
                elif diff_type == 'diff':
                    diff = unified_diff(old_file_data, new_file_data, n=0)
                    diff_file += '.diff'
                elif diff_type == 'html':
                    diff = HtmlDiff().make_file(fromlines=old_file_data,
                                                tolines=new_file_data,
                                                fromdesc=old_file,
                                                todesc=new_file,
                                                context=True,
                                                numlines=0)
                    diff_file += ".html"
                with(open(diff_file, 'w+')) as fw:
                    fw.write(''.join(diff), )
                
                if ( ext == '.pdf'):
                    sys.stdout.write('removing file')
                    silentremove(old_file)
                    silentremove(new_file)

            sys.stdout.write("{0}, done\n".format((input_data[0])))
            return {'status': 'Fail', 'file': os.path.split(old_file)[1],
                    'diff': '<a target=\"_blank\" href=\"%(diff)s\">%(diff)s</a>' % {
                        'diff': os.path.join('diffs', os.path.split(diff_file)[1])}}
        else:
            sys.stdout.write("{0}, done\n".format(old_file))
            return {'status': 'Pass', 'file': os.path.split(old_file)[1], 'diff': None}
    except Exception as e:
        print(e)
        return {'status': 'Fail', 'file': os.path.split(old_file)[1], 'diff': None}


# @do_cprofile
def main():
    # lets read the conf file and validate all the parameters

    parser = OptionParser()
    parser.add_option("-c", "--conf", dest="conffile", help="conf file")

    options= parser.parse_args()[0]

    if not options.conffile:  # if filename is not given
        parser.error('configuration file not given')
    conf_parse = ConfigParser()
    conf_parse.read(options.conffile)

    old_folder = conf_parse.get('conf', 'old_folder')
    new_folder = conf_parse.get('conf', 'new_folder')
    report_folder = conf_parse.get('conf', 'report_folder')
    diff_type = conf_parse.get('conf', 'diff_type')
    helpers = int(conf_parse.get('conf', 'helpers'))

    # Lets get all the files from both the folders
    old_files = [f for f in os.listdir(old_folder)]
    new_files = [f for f in os.listdir(new_folder)]

    # finds the files which are common in both the folders
    sold = set(old_files)
    snew = set(new_files)

    common_files = list(sold.intersection(snew))
    missing_files_old = list(sold.difference(snew))
    missing_files_new = list(snew.difference(sold))
    # common_files = [x for x in old_files if x in new_files]
    # missing_files_old = list(set(old_files) - set(new_files))
    # missing_files_new = list(set(new_files) - set(old_files))
    # Lets remove all the files with zero file size
    size_zero = get_zero_size_common_files(common_files, old_folder, new_folder)

    for a in size_zero:
        common_files.remove(a['file'])

    task_list = []
    diffs = os.path.join(report_folder, 'diffs')
    if not os.path.exists(diffs):
        os.mkdir(diffs)
    for file_name in common_files:
        task_list.append([os.path.join(old_folder, file_name),
                          os.path.join(new_folder, file_name),
                          diffs, diff_type])
    global filecount
    filecount = len(common_files)
    if filecount > helpers:
        pool = Pool(helpers)
    else:
        pool = Pool(filecount)
    results = pool.map(compare_file, task_list)
    # lets start generating the json files
    #1. missing file list
    #2. compare report
    #3. zero size report
    #4. failed reports -> inside compare report
    lst = []
    for miss in missing_files_old:
        di = {'file': miss, 'miss': 'old'}
        lst.append(di)

    for miss in missing_files_new:
        di = {'file': miss, 'miss': 'new'}
        lst.append(di)
    miss_json = os.path.join(report_folder, 'miss_list.json')
    with open(miss_json, 'w+') as fw:
        json.dump(obj=lst, fp=fw, sort_keys=True)

    failed = []
    for res in results:
        if res['status'] == 'Fail' and res['file'] == '':
            failed.append(res)
            results.remove(res)

    failed = sorted(failed, key=itemgetter('file'))
    failed_json = os.path.join(report_folder, 'failed.json')
    with open(failed_json, 'w+') as fw:
        json.dump(obj=failed, fp=fw)

    result1 = sorted(results, key=itemgetter('file'))
    result_json = os.path.join(report_folder, 'result.json')
    with open(result_json, 'w+') as fw:
        json.dump(obj=result1, fp=fw)

    size_zero = sorted(size_zero, key=itemgetter('file'))
    size_zero_file = os.path.join(report_folder, 'size_zero.json')
    with open(size_zero_file, 'w+') as fw:
        json.dump(obj=size_zero, fp=fw)

    copy_report_files(os.path.split(os.path.realpath(__file__))[0], report_folder)


if __name__ == '__main__':
    main()
