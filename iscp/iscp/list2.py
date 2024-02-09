# create a list and sorted
a=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    i=int(input("enter the element"))
    a.append(i)
print(a)
for i in a:
    for j in a:
        if i>j:
            temp=i
            i=j
            j=temp
print(a)