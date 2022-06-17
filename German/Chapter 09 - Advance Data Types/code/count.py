s = "Anshu"
print( 'Size of %s => %d' % (s, len(s)))
print(dir(s))
print( 'Size of %s => %d' % (s, s.__len__()))

def size(strdata):
    c = 0
    for a in strdata:
        c+=1
    return c

print(size(s))