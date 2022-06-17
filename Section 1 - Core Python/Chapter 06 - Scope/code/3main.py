a = 10


def test():
    a = "Pune Rocks"
    print(a)
    print(locals())
    print(globals())
    

def test2():
    print(a)


test()
print("")
test2()
