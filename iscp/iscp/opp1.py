# cook your dish here
t=int(input())
for i in range(0,t):
    n=int(input("enter").split(" "))
    m=int(input().split(" "))
    k=int(input().split(" "))
    if n+k<=m:
        print("YES")
    else:
        print("NO")