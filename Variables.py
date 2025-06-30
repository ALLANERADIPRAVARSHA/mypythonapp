list1=[]
for i in range(n):
    ifi%2==0:
        list1.append(i)
print(list1)
list2=[x for x in range(n) if x%2==1]
print(list2)