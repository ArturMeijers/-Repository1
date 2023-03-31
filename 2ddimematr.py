size = int(input("Enter the size of the 2D list: "))

# create a 2D list with the given size
matrix = [[0] * size for _ in range(size)]

# populate the matrix with multiplication table values
for i in range(size):
    for j in range(size):
        matrix[i][j] = (i+1) * (j+1)

# print the matrix
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()