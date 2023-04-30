# mytuple=(10,20,30,40,50,60,70,80,90,"ctoo")
# my_list=list(mytuple)
# print(my_list)
# print(mytuple[0]+mytuple[2:])
int_str = input("Enter the 10 elements separated by space: ")
list2 = int_str.split()
if len(list2) == 10:
    tuple_1 = tuple(map(int, list2))
    index = int(input("Enter the index of the element to delete: "))
    tuple_1 = tuple_1[:index]+tuple_1[index+1:]
    print("After deleting the element:", tuple_1)
else:
    print("Please enter 10 elements!")