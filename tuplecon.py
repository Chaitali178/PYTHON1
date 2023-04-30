my_tuple=input("Enter words separated by spaces: ").split()
my_tuple1=input("Enter words separated by spaces: ").split()
print('Tuple1:', my_tuple)
print('Tuple1:', my_tuple1)
tup1=list(my_tuple)
tup2=list(my_tuple1)
tup1.extend(tup2)
print("Tuples after concatinating: "+str(tuple(tup1)))

