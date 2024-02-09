x,y=map(int,input().split())

res=1
while(y>0):
    if y%2==0:
        res*=x
    x=x*x
    y//2
print(res)