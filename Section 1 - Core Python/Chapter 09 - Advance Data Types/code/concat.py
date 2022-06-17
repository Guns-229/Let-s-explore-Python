s = 'Camel'
print(id(s))
s = 'The ' + s + ' ran away!'
# Concatenation
print(s)
print(id(s))
st = 'The ' + s + ' ran away!'
print(st)
print(id(st))
print(id(s))