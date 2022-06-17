import utils

files_short = ["lst1.txt", "lst2.txt"]
files_long = ["lstlong1.txt", "lstlong2.txt"]
files = files_short
lst = {}
for fname in files:
    with open(fname) as f:
        lst[fname] = f.read().splitlines()

common_data = utils.compare_intersect(lst[files[0]], lst[files[1]])
print("common data count (compare_intersect):", len(common_data))
with open("common_data.txt", "w+") as f:
    f.write(str(list(common_data)))

common_data = utils.compare_listcomp(lst[files[0]], lst[files[1]])
print("common data count (compare_intersect):", len(common_data))

common_data = utils.compare_bitwise(lst[files[0]], lst[files[1]])
print("common data count (compare_bitwise):", len(common_data))

# utils.simple_compare(lst[files[0]], lst[files[1]])
