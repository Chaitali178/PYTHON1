print("-----Marksheet Grades-----")
b=int(input("Enter The Marks"))
def marks(n):
 if b>=80:
   print("First Class")
 elif b<80 and b>=70:
   print("Second Class")
 elif b<70 and b>=60:
   print("Average")
 elif b<60 and b>=40:
   print("Pass")
 else:
   print("Fail")
marks(b)
