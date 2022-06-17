def outer():
    a = 0
    b = 22

    def inner():
        print(locals())
        print(globals())

    inner()


outer()
