import copy

class MyTry:
    def __init__(self):
        self.lst = [1,2,3,4,5]

a = MyTry()
dup = copy.copy(a)
a.lst.append(6)
print(a.lst, dup.lst)
print(id(a), id(dup))
print(id(a.lst), id(dup.lst))
