
def listing(num, lst):
	lst = list(lst)
	lst[1].append(num)
	return True

l = [1, [2], 3]
b = listing(10, l)
print(l, b)