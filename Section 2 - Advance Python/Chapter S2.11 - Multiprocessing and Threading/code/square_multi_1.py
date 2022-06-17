from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def doubleMe(x):
    return x ** x

y = range(10000)

def test():
    pool = ThreadPool(10) 
    # Open the urls in their own threads
    # and return the results
    results = pool.map(doubleMe, y)
    #close the pool and wait for the work to finish 
    pool.close() 
    pool.join() 
    

if __name__=='__main__':
    from timeit import Timer
    t = Timer("test()", "from __main__ import test")
    print (t.timeit(number=5))

