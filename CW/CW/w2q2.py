n=input("codeword 1: ")
m=input("codeword 2: ")
a=[]
b=[]

if len(n)!=len(m):
    print("-1")
else:
    for i in n:
        a.append(i)
    for j in m:
        b.append(j)
    for k in range(0,len(n)):
        if a[k]==b[k]:
            print("0",end="")
        else:
            print(1,end="")



