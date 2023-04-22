n=int(input("Enter the number of rows"))
def patternp1(n):
    a=0
    for i in range (n,0,-1):
        a+=1
        for j in range(1,i+1):
            print("*", end="")
        print()
patternp1(n)
  