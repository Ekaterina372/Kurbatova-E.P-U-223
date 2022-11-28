x=int(input("Первое число "))
y=int(input("Второе число "))
i=1
while x<=y:
    if x==y:
        break
    x+=x/10
    i+=1
print(i)