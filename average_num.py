def calculate_average(lst):
    if len(lst) == 0:
        return None
    total = sum(lst)
    average = total / len(lst)
    return average

numbers=list(map(int,input("Enter the elements: ").strip().split()))

average = calculate_average(numbers)
if average is None:
    print("The list is empty.")
else:
    print(f"The average of the numbers is: {average}")