num = 10

def test():
	global num
	x = "Vadakkam"
	print(x)
	print(locals())
	num = 20


print(locals())
print(id(test))
test()
print(num)
