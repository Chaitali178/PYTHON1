n=int(input("Enter the number of rows"))
def patternp1(n):
    for i in range (1,n+1):
        for j in range(1,i+1):
            print("*", end="")
        print()
patternp1(n)
  