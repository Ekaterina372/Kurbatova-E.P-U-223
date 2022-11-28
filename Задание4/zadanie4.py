a = int(input("Первое чило:"))
b = int(input("Второе число:"))
for i in range(a, b + 1):
    print(i)

a = int(input("Первое чило:"))
b = int(input("Второе число:"))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

a = int(input("Первое чило:"))
b = int(input("Второе число:"))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')

n = int(input("кол-во чисел:"))
sum = 0
for i in range(n):
    sum += int(input("целые числа:"))
print(sum)

n = int(input("Введите число:"))
s = 0
for i in range(1, n+1):
    s += i ** 3
print(s)

res = 1
n = int(input("Введите число: "))
for i in range(1, n + 1):
    res *= i
print(res)


n = int(input("введите число: "))
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)

n = int(input("Введите число:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()

def task(n):
   s,c,p=0,0,1
   for _ in range(n):
      c,p=c+p,c
      s+=c
   return s 
 
n=int(input("n="))
print(task(n))



    