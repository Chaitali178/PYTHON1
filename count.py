c=str(input("Enter the string:"))
count=0
for i in range(0,len(c)):
    if(c[i]!=''):
      count=count+1
print("Total number of characters in a string are: "+str(count))
