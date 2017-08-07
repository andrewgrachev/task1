# Задание 1:
# Написать программу вычисления n-го числа Фибоначчи,
# используя операции над матрицами из Numpy.

import numpy

print('please input n in F(n) Fibonacci sequence')
c = int(input()) + 1


def mm_fib(n):
    return (numpy.matrix([[2, 1], [1, 1]]) ** (n // 2))[0, (n + 1) % 2]


for i in range(c):
    print(mm_fib(i))