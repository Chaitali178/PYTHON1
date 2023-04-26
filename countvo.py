str=str(input("Enter the string:"))
def count_vowel(str):
     count=0
     vowel='a', 'e','i','o','u','A','E','I','O','U'
     for alphabet in str:
        if alphabet in vowel:
            count=count+1
     print("No. of Vowels in a given string are: ",count)
count_vowel(str)
