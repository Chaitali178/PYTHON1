list=[]
n=int(input("Enter number of elements: "))
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print(list)
my_tuple=tuple(list)
print(my_tuple)