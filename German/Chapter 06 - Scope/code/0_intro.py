month = 7
year = 1947

def A():
    month = 3
    date = 10
    print(locals())
    print(globals())

def B():
    month = 2
    date = 15
    print(locals())
    print(globals())

A()
B()
