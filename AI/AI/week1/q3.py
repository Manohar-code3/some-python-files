row=int(input("enter the no of rows= "))
col=int(input("enter the no of colomns= "))

matrix=[]

for i in range(row):
    m1=[]
    for j in range(col):
        num=int(input(f"enter the matrix[{i}][{j}]"))
        m1.append(num)
    matrix.append(m1)
print("matrix :")
for i in matrix:
    print(i)
count=0
for i in matrix:
    for j in i:
        if j==0:
            count+=1
print("no of zero`s in matrix = ",count)