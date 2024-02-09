n=input("enter the polynomail")
l=[]
for i in n:
    l.append(i)
print(l)
for i in l:
    if i=="x":
        l.remove(i)
print(l)