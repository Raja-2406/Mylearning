salary=int(input("Enter Your Salary :"))
age=int(input("Enter your age"))
if(salary>=20000 or age<=25):
    loan=int(input("Enter your loan Amount"))
    if(loan>50000):
        print("MAximum loan Amount is 50000")
else:
    print("You are Not Eligible for loan")
