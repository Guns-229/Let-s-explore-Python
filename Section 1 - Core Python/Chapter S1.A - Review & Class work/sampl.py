# x, y = "Testing" " is good", ". Lets do it"
# print(x, y)

# x = "Shri" 
# y = "Raman" 
# print(x.join(" ").join(y)) 

# x = {}
# d = (10, 20, [2])
# x[d] = "test"
# print(x)

x = {"Ron", "Ron", "Road"} 
print(x)

lst = list() 
print(type(lst))

a, b, c, d = 256, 256, 1000, 1000
print(a is b, c is d)

def listing(num, lst):
	lst.append(num)
	return lst

l = [1, 2, 3]
b = listing(4, l)
print(l, b)

x = [1, 2, 3, 4, 5]
x[::2] = 3, 6, 10
print(x)

def listing(num, l): 
	lst = list((l,)) 
	lst.append(num)
	return lst

l = []
l, b = listing(10, l), [1, 2, 3] 
print(l, b)


def echo(one, *sec): 
    print(one, sec) 
 
echo(list(range(1, 20, 5))) 