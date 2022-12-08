import math

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

def result(x, n):
    res =  (x**n) / fac(n)

    return res

print('результат выражения x^n/n! =  ' + str(result(5, 6)))