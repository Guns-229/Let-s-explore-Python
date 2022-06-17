num = 10

def test():
	global num
	x = "Vadakkam"
	print(x)
	print(globals())
	num = 20


print(globals())
test()
print(num)
