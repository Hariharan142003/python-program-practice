#the code for find the factorial of a number using for loop

n=int(input("enter the number:"))
res=1
for i in range(1,n+1):
    res=res*i
print("the factorial of the number is:",res)

#the code for find the factorial of a number using for loop
n=int(input("enter the number:"))
res=1
i=1
while i<=n:
    res=res*i
    i+=1
print("the factorial of the number is:", res)
