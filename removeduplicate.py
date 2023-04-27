def remove(duplicate):
    resulting_list=[]
    for num in duplicate:
       if num not in resulting_list:
          resulting_list.append(num)
    return resulting_list
duplicate= input("Enter the numbers:")
duplicate=duplicate.split(" ")
print(remove(duplicate))
