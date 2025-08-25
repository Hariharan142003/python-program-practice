# Palindrome Number Checker

# Take input from user
n = int(input("Enter a number: "))

# Store original number
s = n
res = 0

# Reverse the number using modulo and integer division
while s != 0:
    rem = s % 10          # Get last digit
    res = res * 10 + rem  # Build reversed number
    s = s // 10           # Remove last digit

# Check if original number and reversed number are same
if n == res:
    print("It is a palindrome number")
else:
    print("It is not a palindrome number")
