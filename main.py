# [i for i, e in enumerate([1, 2, 1]) if e == 1]
list1=[1,2,1,2,3,4,5,1,2,3,1]
list2=[]
for i,a in enumerate(list1):
    if a==1:
        list2.append(i)

print(list2)