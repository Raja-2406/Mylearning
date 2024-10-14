username="Sunshine"
password="royce"

def validate():
    if(uname==username and passw==password):
        return True
    else:
        return False

uname=input("enter the correct username")
passw=input("enter the correct password")

print(validate())
