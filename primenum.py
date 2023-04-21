a=int(input("Enter the start range:"))
b=int(input("Enter the End range:"))
print("The prime numbers between",a,"and",b,"are:")
for num in range(a,b):
        if num>1:
            for i in range(2,num):
             if (num%i)==0:
                break
            else:
                print(num)