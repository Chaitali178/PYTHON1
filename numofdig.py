n=int(input("Enter the number: "))
count=0
a=n
for i in str(a):
    count=count+1
    a=a//10
print("The number of digit in the number are:",count)
