a=int(input())
add=0
temp=a

while(temp!=0):
    r=temp%10
    add=add+r
    temp=temp//10
if(add==a):
    print(a,"is a perfect number")
else:
    print("hai")
