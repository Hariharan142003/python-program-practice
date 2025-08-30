#program to count a number of vowels in the word or sentence
n=input("Enter the word: ")
count=0
for i in n:
    if i=='a' or i=='e' or i== 'i' or i=='o' or i=='u':
        count+=1
print("the total number of vowels in the word is:", count)



