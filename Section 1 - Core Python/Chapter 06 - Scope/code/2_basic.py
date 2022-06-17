"""
How to update the global variable from within the function
"""
num = 10


def test():
    global num
    num = 20
    print(num)


test()
print(num)
