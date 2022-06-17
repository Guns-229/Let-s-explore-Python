vals = [1, -10, 30, -4, 12]


def sortme(num):
    if num >= 0:
        return 1
    else:
        return 0


vals.sort(key=sortme, reverse=True)
print(vals)

a = {1: 2, 2: 3}
b = {1: 3, 4: 5}

d = set(a).intersection(b)
print(d)

a = {"a": 1, "b": 2}
b = {"c": 3, "a": 4}
a.values()
k1 = a.keys()
k2 = b.keys()

c = k1.append(k2)
print(k1)
