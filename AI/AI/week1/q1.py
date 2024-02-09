def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element at position ({i}, {j}): "))
            row.append(value)
        matrix.append(row)
    return matrix

def sum_of_rows(matrix):
    row_sums = []
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums

def sum_of_columns(matrix):
    col_sums = []
    num_cols = len(matrix[0])
    
    for j in range(num_cols):
        col_sum = sum(matrix[i][j] for i in range(len(matrix)))
        col_sums.append(col_sum)
    
    return col_sums

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix = read_matrix(rows, cols)
    
    print("\nMatrix:")
    for row in matrix:
        print(row)
    
    row_sums = sum_of_rows(matrix)
    col_sums = sum_of_columns(matrix)
    
    print("\nSum of rows:")
    for i, row_sum in enumerate(row_sums):
        print(f"Row {i + 1}: {row_sum}")
    
    print("\nSum of columns:")
    for j, col_sum in enumerate(col_sums):
        print(f"Column {j + 1}: {col_sum}")

