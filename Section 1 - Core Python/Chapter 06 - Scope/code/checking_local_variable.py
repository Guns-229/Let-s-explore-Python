a = 10

def test(b=[]):
    global a
    x = 10
    print("Checking if x is a local variable:", 'x' in locals())
    print("Checking if a in a local variable:", 'a' in locals())
test(("a"))
print(a)
