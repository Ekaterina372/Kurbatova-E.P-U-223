arr=[1,0,3,4,0,5,6,0,8,9,10]



def result(arr):
    srAr =  sum(arr)/len(arr)
    for i in range(len(arr)):
        
        if arr[i] == 0:
            arr[i] = srAr

    return arr

print('максимальный элемент: ' + str(result(arr)))