


class MyDict(dict):
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)

        return val

    def __setitem__(self, key, val):
        print('SET', key, val)
        dict.__setitem__(self, key, val)

    def __repr__(self):
        dictrepr = dict.__repr__(self)
        return '%s(%s)' % (type(self).__name__, dictrepr)

    def update(self, *args, **kwargs):
        print('update', args, kwargs)
        for k, v in dict(*args, **kwargs).items():
            self[k] = v


md = MyDict({1: 2, 2: 3, 3: 4, 10: 10, 5: 5})

print(md)

for d in md:
    print(d)
