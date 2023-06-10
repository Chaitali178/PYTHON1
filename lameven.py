is_even=lambda num: num%2==0
number=int(input("Enter a number:"))
result=is_even(number)
if result:
    print(number,"is even.")
else:
    print(number,"is odd.")