test=str(input("Enter the string "))
print("The original string is: ",test)
common_char={}
for i in test:
    if i in common_char:
        common_char[i]+=1
    else:
        common_char[i]=1
result=max(common_char,key=common_char.get)
print("The maximum of all characters is: "+str(result))