number=int(input("Enter the range: "))
i=0
a=0
b=1
while(i<number):
    if(i<=1):
        next=i
    else:
        next=a+b
        a=b
        b=next
    print(next)
    i=i+1