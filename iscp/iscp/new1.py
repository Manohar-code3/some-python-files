n=4
a=[]
count=0
for i in range(0,n):
    # a[i]=int(input())
    i=int(input("enter the elements"))
    a.append(i)
diff=int(input("enter the diff"))
for j in a:
    if((j+1)-(j))==diff:
        count+=1
    else:
        count=1
print(count)

