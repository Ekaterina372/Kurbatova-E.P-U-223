prev = int(input("Введите число "))
answer = 0
while prev != 0:
    next = int(input("Введите число "))
    if next != 0 and prev < next:
        answer += 1
    prev = next
print(answer)