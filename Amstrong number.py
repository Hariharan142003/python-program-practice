#program to find amstrong number from range of 1 to 100
for i in range(100):
    num=i
    result=0
    n=len(str(i))
    while i!=0:
        digit=i%10
        result=result+digit**n
        i=i//10
    if result==num:
        print(num)
