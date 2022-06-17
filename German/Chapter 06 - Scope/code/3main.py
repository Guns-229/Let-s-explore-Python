global a
a = 10

def test():
    a = "Pune Rocks"
    print(a)
    print(locals())
    print(globals())
    
def test2():
    b = "TEST"
    print(locals())
    print(globals())

test()
print("")
test2()
