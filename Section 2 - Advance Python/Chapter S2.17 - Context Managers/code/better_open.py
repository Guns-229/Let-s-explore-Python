file_list = []
for x in range(99999):
    fp = open('foo.txt', 'w')
    fp.close()
    file_list.append(fp)
print(file_list[:10])
