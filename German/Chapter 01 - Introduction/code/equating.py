a = b = 'Amit Shrivastava'
print(a is b)
print(a == b)

a = 'Amit Shrivastava'
b = ['A', 'm', 'i', 't', ' ', 'S', 'h', 'r', 'i', 'v', 'a', 's',
     't', 'a', 'v', 'a']
print(a is "".join(b))
print(a == "".join(b))
