n=input("input codeword 1 : ")
m=input("input codeword 2 : ")
a=[]
b=[]
count=0
if len(n)!=len(m):
    print("-1")
else:
    if n==m:
        print("0")

    else:
        for i in n:
            a.append(i)
        for j in m:
            b.append(j)
        for k in range(0,len(n)):
            if a[k]!=b[k]:
                count+=1
        print(count)

