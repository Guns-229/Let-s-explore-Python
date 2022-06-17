class Test(object):
    def __init__(self, mydata):
        self.mydata = mydata

a = [1, 2, 3]
b = [1, 2, 3]

ta = Test(a)
tb = Test(b)

print(ta.mydata, id(ta.mydata))
print(tb.mydata, id(tb.mydata))

