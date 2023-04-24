string=str(input("Enter the string:"))
vowels=['a','e','i','o','u','A','E','I','O','U']
remove_vowel=""
for i in range(len(string)):
    if string[i] not in vowels:
        remove_vowel=remove_vowel+string[i]
print("After removing Vowels the string is:",remove_vowel)