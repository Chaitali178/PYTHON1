numbers=list(map(int,input("Enter the elements: ").strip().split()))
max_number=lambda nums:max(nums)
print("Maximum value from a list of numbers is: ",max_number(numbers))