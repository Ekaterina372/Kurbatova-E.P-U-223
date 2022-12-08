
def fac():
   
    digit = int(input('число >>>  '))
    if(digit == 0):
        return 0
    else:
        return max(digit, fac())


print(fac())
