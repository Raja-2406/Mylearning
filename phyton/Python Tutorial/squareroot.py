a=int(input("Enter a positive Number :"))
if(a<0):
    print("Enter a valid number")
else:
    
    countt=0
    first=0
    second=1
    while(count<a):
        print(first,end=" ")
        next=first+second
        first=second
        second=next
        countt+=1
