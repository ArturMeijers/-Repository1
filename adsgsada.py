# Ask user for number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Create an empty matrix with 0s
matrix = [[0 for j in range(columns)] for i in range(rows)]

# Populate the matrix with multiplication tables
for i in range(rows):
    for j in range(columns):
        result = (i+1) * (j+1)
        equation = str(i+1) + " x " + str(j+1)
        matrix[i][j] = "{0:4d} ({1})".format(result, equation)

# Print the matrix
for row in matrix:
    for item in row:
        print(item, end="\t")
    print()