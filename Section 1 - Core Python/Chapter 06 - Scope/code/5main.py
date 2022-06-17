global a
a = 10

def test():
    a = "Pune Rocks"
    print(a)
    print(locals())
    print("~"*20)
    print(globals())
    
test()
print(a)

