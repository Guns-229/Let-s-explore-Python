x = 0
def outer():
    nonlocal x
    x = 1
    def inner():
        nonlocal x
        x = 2
        print("inner:", id(x))

    inner()
    print("outer:", id(x))

outer()
print("global:", id(x))

# inner: 2
# outer: 2
# global: 0
