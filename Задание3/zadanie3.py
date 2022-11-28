a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
s = a + b + c
print(s)

a = int(input("Длина первого катета:"))
b = int(input("Длина второго катета:"))
print(1/2 * a*b)

n = int(input("Введите минуты:"))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

a = int(input("Расстояние между рядами:"))
b = int(input("Расстояние между дырочками:"))
l = int(input("Количество дырочек:"))
N = int(input("Длина свободного конца шнурка:"))
print(2 * l + (2 * N - 1) * a + 2 * (N - 1) * b)

a = int(input("Первое число:"))
b = int(input("Второе число:"))
c = int(input("Третье число:"))
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)

x1 = int(input("Первая координата белой:"))
y1 = int(input("Первая координата черной:"))
x2 = int(input("Вторая координата белой:"))
y2 = int(input("Вторая координата черной:"))
if ((x1 + y1) % 2) == ((x2 + y2) % 2):
    print('Да')
else:
    print('Нет')

year = int(input("Задайте натуральное число:"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('Да')
else:
    print('Нет')

a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
c = int(input("Введите третье число:"))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

n = int(input("Перое кол-во долек:"))
m = int(input("Второе кол-во долек:"))
k = int(input("Третье кол-во долек:"))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да')
else:
    print('Нет')

