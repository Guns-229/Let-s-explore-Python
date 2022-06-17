import os
from timeit import timeit
from functools import reduce

def fun_sum_it(num):
    total = 0
    for a in range(num):
        total +=a
    return total

def fun_sum_it_updated(num):
    return sum(range(num))

print(fun_sum_it(100))
print(fun_sum_it_updated(100))
