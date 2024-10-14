num=int(input("Enter an number 1  :"))
num2=int(input("Enter an number 2 :"))
operation=input("Add or Subract or Multiply or Divison")
if(operation=="Add"):
    print(num+num2)
elif(operation=="Subract" or operation=="subract"):
    print(num-num2)
elif(operation=="Multiply"):
    print(num*num2)
elif(operation=="Divison"):
    print(num/num2)
else:
    print("Enter an Valid operation")
