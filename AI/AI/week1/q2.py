row=int(input("enter the rows="))
col=int(input("enter the coloums="))
matrix =[]
for i in range(row):
    m1=[]
    for j in range(col):
        num=int(input(f"enter the matix[{i}][{j}]="))
        m1.append(num)
    matrix.append(m1)
# print(matrix)
print("matrix  :")
for i in matrix:
    print(i)

row_sum=[]
for rows in matrix:
    rows_sum=sum(rows)
    row_sum.append(rows_sum)
for i in row_sum:
    print("sum of row = ",i)

col_sum=[]
num_rows=len(matrix)
num_col=len(matrix[0])
for j in range(num_col):
    col_sums=0
    for i in range(num_rows):
        col_sums+=matrix[i][j]
    col_sum.append(col_sums)
for i in col_sum:
    print("sum of rows=",i)

