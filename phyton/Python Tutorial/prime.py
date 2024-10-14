def palindrome(n):
    return str(n)==str(n)[::-1]
def nexpalli(n):
    n+=1
    while not palindrome(n):
        n+=1
    return(n)
a=int(input())

if(palindrome(a)):
    print("Already a pallindrome")
else:
    print(nexpalli(a))
