import glob
import subprocess

FORMAT = "pdf"


def exportPdf(srcFile):
    # folder = srcFile
    cmd = "jupyter nbconvert --to %s \"%s\"" % (FORMAT, srcFile)
    print(cmd)
    print(subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout.read())


lstFiles = []
for filename in glob.iglob('**/*.ipynb', recursive=True):
    lstFiles.append(filename)
    exportPdf(filename)
