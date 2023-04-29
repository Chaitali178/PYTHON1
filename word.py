str=input("Enter the string")
count_word={}
character=str.split()
for word in character:
    if word in count_word:
        count_word[word]+=1
    else:
        count_word[word]=1
for word,con in count_word.items():
    print(word,count_word)