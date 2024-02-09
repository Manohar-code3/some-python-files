p=int(input())
q=int(input())
x,y=map(int,input().split())
while(x!=y):
    if x<y:
        x+=p
    else:
        y+=q
print(x)
