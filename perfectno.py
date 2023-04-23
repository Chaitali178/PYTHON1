n=int(input("enter the number:"))
add=0
for i in range(1,n):
    if(n%i==0):
        add=add+i
if add==n:
    print("The number",n,"is a Perfect Number")
else:
    print("The number",n,"is not Perfect")       

