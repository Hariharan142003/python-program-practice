#program to remove a given character from a string(using for loop)
word=input("enter a word:")
letter=input("enter the letter to remove:")
result=[]
for i in word:
    if i!=letter:
        result.append(i)
result="".join(result)
print("the word after removing the letter:", result)

#program to remove a given character from a string(using while loop)
word = input("Enter a word: ")
letter = input("Enter the letter to remove: ")
result = ""
i = 0
while i < len(word):
    if word[i] != letter:
        result += word[i]
    i += 1

print("The word after removing the letter:", result)
