n=int(input("Enter the number: "))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=0
for dig in str(n):
    num+=fact(int(dig))
if num==n:
    print(n,"is a strong number")
else:
    print(n,"is not a strong number")

