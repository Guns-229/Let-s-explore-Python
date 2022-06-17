# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 06:19:01 2017

@author: johri_m
"""

import os
import subprocess
import shutil
from optparse import OptionParser


def execute(cmd):
    """Execute.

    Purpose  : To execute a command and return exit status
    Argument : cmd - command to execute
    Return   : exit_code
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    (result, error) = process.communicate()

    rc = process.wait()

    if rc != 0:
        print("Error: failed to execute command:", cmd)
        print(error)
    return result


htmlFiles = []
parser = OptionParser()
parser.add_option("-s", "--source", dest="source",
                  help="parent source directory", metavar="source")
parser.add_option("-d", "--dest", dest="dest",
                  help="destination directory")

(options, args) = parser.parse_args()

md_files = []
for d in os.walk(options.source):
    for f in d[2]:
        if f.endswith(".ipynb") and "-checkpoint" not in f:
            print("Processing: ", f)
            file_name = os.path.join(d[0], f)
            execute("jupyter nbconvert --to Markdown \"" + file_name + "\"")
            file_name_md = os.path.splitext(file_name)[0] + ".md"
            md_files.append(file_name_md[2:])
            htmlFiles.append(os.path.abspath(file_name_md))

cwd = os.getcwd()
dest = options.dest
print("options.dest" + dest)
htmlFiles.sort()
for f in htmlFiles:
    print("Copying file:", f)
    d = os.path.split(f.split(cwd)[1])[0][1:]
    dest_path = os.path.join(dest, d)
    print("path", dest_path)
    os.makedirs(dest_path, exist_ok=True)
    shutil.copy(f, dest_path)

# Now lets create the summary file
# currently it will work on simple files without subfolder.
md_files.sort()
with open(os.path.join(dest,"summary.md"), "w") as summary_file:
    summary_file.write("# Summary\n")
    for loc in md_files:
        base = os.path.basename(loc)
        name = os.path.splitext(base)[0]
        summary_file.write("* [{name}]({loc})\n".format(name=name,
                                                        loc=loc))
#with open("../content/summary.md", "w") as summary_file:
#    summary_file.write("# Summary\n")
#    for loc in md_files:
#        base = os.path.basename(loc)
#        name = os.path.splitext(base)[0]
#        summary_file.write("* [{name}]({loc})\n".format(name=name,
#                                                        loc=loc))
