def isprime(n):
    if n==2 or n==3 :
        return 1
    if n==1 or n%2==0 or n%3==0:
        return 0
    for i in range(5,n+1):
        if n%i==0 or n%(i+2)==0:
            return 1
n=int(input())
if isprime(n):
        print("prime")
else:
    print("non prime")