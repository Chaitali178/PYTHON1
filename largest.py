a= int(input("Enter the number: "))
b= int(input("Enter the number: "))
c= int(input("Enter the number: "))

def big(n1,n2,n3):
    if a > b:
        print(a,"is greatest")
    elif c > b:
        print(c,"is greatest")
    else:
        print(b,"is greatest")
big(a,b,c)