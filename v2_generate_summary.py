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

print("options.dest" + options.dest)
for d in os.walk("."):
    for f in d[2]:
        if f.endswith(".md") and "node_modules" not in f:
            print("Processing: ", f)
            file_name = os.path.join(d[0], f)
            md_files.append(file_name)


def get_str(name):
    return name.count(os.sep)


# Now lets create the summary file
# currently it will work on simple files without subfolder.
md_files.sort()
with open(os.path.join(options.dest, "SUMMARY.md"), "w") as summary_file:
    summary_file.write("# Summary\n")
    old = ""
    for loc in md_files:
        print(options.dest)
        rel = loc.split(options.dest)[1]
        base = os.path.basename(loc)
        name = os.path.splitext(base)[0]
        chapter = rel.split(os.sep)[0]
        if old != chapter:
            txt = "* \\[{}\\]\n".format(chapter)
            summary_file.write(txt)
            old = chapter
        print(rel, get_str(rel), base, name)
        tabs = "\t" * get_str(rel)
        txt = "{tabs}* [{name}]({loc})\n".format(name=name,
                                                 loc=loc,
                                                 tabs=tabs)
        summary_file.write(txt)
