import math
a=int(input())
flag=1
if a<0:
    print("Enter a valid number")
else:
    for i in range(2,int(math.sqrt(a))+1):
        if(a%i==0):
            print(f"The given number {a}is a composite number")
            flag=0
            break;
    if flag:
        print(f"The given number {a} is a prime number")
