def equally(n):
    count=0
    mini=-1
    maxi=0
    while n !=0:
        if mini == n:
            count = count + 1
        else:
            mini = max(maxi, count)
            count = 1
        n = int(input())
    maxi = max(maxi, count)
    print("Максимальное поряд: ", maxi)
equally(int(input("Максимальное поряд: ")))
