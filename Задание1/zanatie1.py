print("Курс Основы программирования начался")

a=16823
b=12302
c=3092
d = a * b % c
print(d)

age = int(input('Укажите свой возраст:'))

if age >= 16 and age < 75 :
    print("Поздравляем вы поступили во ВГУИТ")

elif age < 16 and age > 0 :
    print("Сначала нужно окончить школу!")

else:
    print("Введите возраст корректно")
if age < 16:
    print('Вам осталось учится в школе', 16-age,'лет')

name = str(input('Укажите свое имя: '))
if name == ('Иван'):
    print('Ваше имя не подходит')

seconds = int(input("Введите кол-во секунд"))

min = seconds // 60
hour = min // 60 
days = hour // 24

print (days, ":", hour, ":", min, ":", seconds)

n= int(input("Укажите число для решения выражения n + n^2 + n^3 + n^4 + n^5:"))
print( n + n**2 + n**3 + n**4 + n**5)

x = 1
y = 2
x,y = y,x
print(x)
print(y)

number = int(input('Введите число:'))
if number % 2 == 0:
    print('Четное число')
else:
    print('Нечетное число')

