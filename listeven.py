def list_even(x):
    even=[]
    for n in x:
        if (int(n)%2)==0:
            even.append(n)
    return even
numbers= input("Enter a list of integers separated by commas:")
x= numbers.split(" ")
print("Even numbers in list are:",list_even(x))

# def get_even_numbers(numbers_list):
#     even_numbers=[]
#     for i in numbers_list:
#         if (int(i)%2)==0:
#             even_numbers.append(i)
#     return even_numbers
# numbers=input("Enter a list of integers separated by commas:")
# numbers_list= numbers.split(",")
# print("Even numbers in the List are:",get_even_numbers(numbers_list))
