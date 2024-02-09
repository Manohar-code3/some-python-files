#implementation of stack
stack=[]
n=int(input("enter the no of elements u want to add="))
for _ in range(0,n):
    s=input("enter the elment=")
    stack.append(s)
print(stack)
m=int(input("enter the no of elements u wnt to pop="))
for _ in range(0,m):
    stack.pop()
print(stack)
if n==m:
    print('stack is empty')