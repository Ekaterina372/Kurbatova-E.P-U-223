arr=[]
n = 5
for i in range(n):
    arr.append(input('Введите число: '))


def maximal(arr):
    maxEl = str(max(arr))
    return maxEl


def rev(arr):
    revArr = str(list(reversed(arr)))
    return revArr

 
print('максимальный элемент: ' + maximal(arr))
print('обратный порядок:' + rev(arr))