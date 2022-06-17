import random
import timeit


student_count = 100
max_marks = 1000
min_marks = 0
semester = 8

# Don't worry about the below code, we will cover them later
marks = [[random.randint(min_marks, max_marks) 
              for _ in range(semester)] 
                 for _ in range(student_count)]

def marks_sum_v1(marks_list):
    total = 0
    for a in range(6):
        total += marks_list[a]
    total *= 0.1
    for a in range(6, 8):
        total += marks_list[a]
    return total

def test():
    student_marks=max(marks, key=marks_sum_v1)
    max_marks_obtained = marks_sum_v1(student_marks)

if __name__ == '__main__':
    print(timeit.timeit("test()", setup="from __main__ import test"))

