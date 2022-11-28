n = int(input("Введите число:"))

i = n
while i > 1:
    if n % i == 0:
        min = i
    i -= 1
print(min)