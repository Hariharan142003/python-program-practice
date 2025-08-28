#program to count occurrence of a character in a string
word = input("Enter a word: ")
letter = input("Enter the letter to count: ")
count = 0
for i in word:
    if i == letter:
        count += 1
print(f"The letter '{letter}' occurs {count} times in '{word}'.")

