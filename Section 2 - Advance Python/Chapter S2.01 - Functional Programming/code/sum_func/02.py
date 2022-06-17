import random
import timeit


student_count = 100
max_marks = 1000
min_marks = 0
semester = 8


def marks_sum_v2(marks_list):
    total = 0
    
    total = sum(marks_list[a]  for a in range(6)) * 0.1
    total +=  sum([marks_list[a] for a in range(6, 8)])
    return total

def test():
    a = max(marks, key=marks_sum_v2)
    x = marks_sum_v2(a)

if __name__ == '__main__':
    # Don't worry about the below code, we will cover them later
    marks = [[random.randint(min_marks, max_marks) 
              for _ in range(semester)] 
                 for _ in range(student_count)]
    print(timeit.timeit("test()", setup="from __main__ import test"))

