from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def doubleMe(x):
    return x ** x

y = range(10000)

def test():
    x = []
    for a in y:
        x.append(doubleMe(a))
    print(len(x))
        
    

if __name__=='__main__':
    from timeit import Timer
    t = Timer("test()", "from __main__ import test")
    print (t.timeit(number=5))

