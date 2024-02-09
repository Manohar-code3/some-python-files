m=int(input(" enter the size of data word : "))
for r in range(0,m):
    if 2**r >= m+r+1:
        break
print("no of redundant  bits :",r)