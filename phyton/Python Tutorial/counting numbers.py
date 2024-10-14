x=int(input())
y=int(input())
count=0
o_count=0
for i in range(x,y):
    if(i%2==0):
        count=count+1
    else:
        o_count=o_count+1
print("The Total Even Numbers",count)
print("The Total Odd Numbers",o_count)
