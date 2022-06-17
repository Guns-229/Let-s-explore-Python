num = 10

def test():
	global num
	x = "Vadakkam"
	print(x)
	g_vals = globals()
	print(f"Globals: {g_vals}")
	print("Locals:", locals())
	num = 20

print(f"Globals in global scope: {globals()}")
print(f"Locals in global scope: {locals()}")
test()
print(num)

