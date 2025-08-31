#this progan is to find the logest word in a string(using def function)
def longerwod(string):
    l=0
    w=''
    words=string.split()
    for word in words:
        if (len(word)>l):
            w=word
            l=len(word)
    return (w,l)
string=input("enter the string: ")
w,l= longerwod(string)
print(w,l)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#this progan is to find the logest word in a string(without using def function)
string=input("enter the string: ")
l=0
w=''
words=string.split()
for word in words:
    if (len(word)>l):
        w=word
        l=len(word)
print(w,l)
