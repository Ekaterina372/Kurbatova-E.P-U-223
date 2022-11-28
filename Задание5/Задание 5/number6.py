sum = 0
len = 0
element = int(input("Введите число "))
while element != 0:
    sum += element
    len += 1
    element = int(input("Введите число "))
print(sum / len)