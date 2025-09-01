#method1
list1=['python','java','data']
list2=['python','apple','orange']
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            list3.append(i)
print(list3)

#method2

list1=['python','java','data']
list2=['python','apple','orange']
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
print(list3)
