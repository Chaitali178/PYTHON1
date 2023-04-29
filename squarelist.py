list=input("Enter the list: ")
square_num=[int(x) for x in list.split()]
list1=[]
for square1 in square_num:
    list1.append(square1**2)
print(list1)