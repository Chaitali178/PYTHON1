numbers=list(map(int,input("Enter the elements: ").strip().split()))
element=int(input("Entr a number to find its number of occurence: "))
def count_occurrences(lst,element):
    count=lst.count(element)
    return count
occurrences=count_occurrences(numbers,element)
print("The element",element,"occurs",occurrences,"times in the list")