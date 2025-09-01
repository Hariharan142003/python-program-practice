#python pprogram to reverse string (using def)
def ReverseString(string):
    rev=""
    for i in string:
        rev=i+rev
    return rev
string=input("enter the word: ")
rev= ReverseString(string)
print(rev)
python pprogram to reverse string (using def)
