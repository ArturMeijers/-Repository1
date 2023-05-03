rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# create a 2D list with zeros
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(0)
    matrix.append(row)


# fill in the matrix with multiplication table values
for i in range(rows):
    for j in range(columns):
        matrix[i][j] = (i+1) * (j+1)

# display the multiplication table
for i in range(rows):
    for j in range(columns):
        print("{:4d}".format(matrix[i][j]), end="\t")
    print()
