num=int(input("Enter the number: "))
a=num
rev=0
while(num>0):
    b=num%10
    rev=rev*10+b
    num=num//10
if(a==rev):
    print("The number is Palindrome")
else:
    print("The number is not a Palindrome")