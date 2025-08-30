#pattern program to print the right angle triangle using number
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#output for the above program
nter the number of rows: 5
1
22
333
4444
55555

#pattern program to print the right angle triangle using star
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#output for the above program
enter the number of rows: 6
*
**
***
****
*****
******
