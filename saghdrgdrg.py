rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# create a 2D list with zeros
matrix = [[0 for j in range(columns)] for i in range(rows)]

# fill in the matrix with multiplication table values and equations
for i in range(rows):
    for j in range(columns):
        equation = f"{i+1} x {j+1}"
        result = (i+1) * (j+1)
        matrix[i][j] = f"{result:4d} ({equation})"

# display the multiplication table
for row in matrix:
    print("\t".join(row))