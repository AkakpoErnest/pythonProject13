from math import sqrt

n= int(input("enter number"))
num = 0
if(n>1):
    for i in range(2,int(sqrt(n)) + 1):
        if (n %i == 0):
            num = 1
            break
    if (num == 0):
        print(n,"is a prime number")
    else:
        (n,"is not a prime number")
else:
    print(n,"is not a prime number")
