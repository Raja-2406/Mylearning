p=float(input())
rate=float(input())
time=float(input())

a=(1+rate/100)
b=a**time
interest=p*b
print(interest)
