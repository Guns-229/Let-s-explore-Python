import gc

print("Lets find the referrers")
a = [10]
print('*** init,     nr of referrers: ', len(gc.get_referrers(a)))
b = []
b.append(a)

print('*** init,     nr of referrers: ', len(gc.get_referrers(a)))
c = []
c.append(a)
print('*** init,     nr of referrers: ', len(gc.get_referrers(a)))
for x in gc.get_referrers(a):
    print(x)
del(b)
print('*** init,     nr of referrers: ', len(gc.get_referrers(a)))
print('get_referents: ', gc.get_referents(c), len(gc.get_referents(c)))
