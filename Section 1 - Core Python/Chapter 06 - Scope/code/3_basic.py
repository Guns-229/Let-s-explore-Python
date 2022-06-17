num = 10


def test():
    global num
    num = 20
    print("locals:", locals())


print("Globals:", globals())
print(id(test))
test()
print(num)
