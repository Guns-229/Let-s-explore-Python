import os
from optparse import OptionParser


htmlFiles = []
parser = OptionParser()
parser.add_option("-s", "--source", dest="source",
                  help="parent source directory", metavar="source")
parser.add_option("-d", "--dest", dest="dest",
                  help="destination directory")

(options, args) = parser.parse_args()

md_files = []

dest = options.dest
print("options.dest" + dest)
for d in os.walk("."):
    for f in d[2]:
        if f.endswith(".md"):
            print("Processing: ", f)
            file_name = os.path.join(d[0], f)
            md_files.append(file_name)

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
