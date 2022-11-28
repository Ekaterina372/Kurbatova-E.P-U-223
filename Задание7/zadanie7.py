arr=[]
n = 5
for i in range(n):
    arr.append(input('Введите число: '))
 
print('максимальный элемент: ' + str(max(arr)))
print('обратный порядок: ' + str(list(reversed(arr))))


'''a = list(map(float, input().split()))
av = sum(a) / len(a)
for i in range(len(a)):
        if a[i] == 0:
           a[i] = av
        print(a[i], end=" ")'''


