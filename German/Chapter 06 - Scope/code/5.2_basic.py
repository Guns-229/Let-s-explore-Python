num = 10

def test():
	global num
	x = "Vadakkam"
	print(x)
	print(locals)
	num = 20

def test1():
	global num
	y = "Vadakkam"
	print(y)
	print(locals())
	num = 20
	
print(globals())
test()
test1()
print(num)
