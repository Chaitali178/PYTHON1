list=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
print("The maximum number in list is: ",max(list))
print("The maximum number in list is: ",min(list))