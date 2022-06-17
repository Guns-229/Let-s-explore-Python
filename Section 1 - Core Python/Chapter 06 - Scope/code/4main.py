def fun_numbers(a):
    print(id(a))
    print(a)
    a += 10
    print(id(a))
    print(a)
    print(locals())

b = 10
fun_numbers(b)
print(id(b))
print(b)
print(locals())
