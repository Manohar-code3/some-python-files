# avaiable=[]
# n=int(input("no of avalible="))
# for i in range(n):
#     a=int(input("enter the avilable="))
#     avaiable.append(a)
# print(avaiable)
maximum=[]
allocation=[]
m=int(input("no of elements="))
for i in range(0,m):
    print("enter the maximum elements")
    b=[int(input()) , int(input()) , int(input())]
    maximum.append(b)
print(maximum)
o=int(input("enter th no of allocation="))
for i in range(0,o):
    print("enter the allocation element")
    c=[int(input()) , int(input()) , int(input())]
    allocation.append(c)
print(allocation)


needs=[]
iteams=[]
for it1,it2 in zip(b,c):
    iteams.append(it2-it1)
    needs.append(iteams)
print(needs)




import 