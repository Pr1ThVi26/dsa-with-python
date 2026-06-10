rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
print("Enter matrix elements:")
for i in range(rows):
    row = []
for j in range(cols):
        value = int(input("Enter element at [" + str(i) + "][" + str(j) + "]: "))
        row.append(value)
        matrix.append(row)
count = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            count += 1
sparse = []
for i in range(count + 1):
    sparse.append([0, 0, 0])
sparse[0][0] = rows
sparse[0][1] = cols
sparse[0][2] = count
k = 1
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != 0:
            sparse[k][0] = i
            sparse[k][1] = j
            sparse[k][2] = matrix[i][j]
            k += 1
print("\nOriginal Matrix:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
print("\nSparse Matrix Representation:")
print("Row\tCol\tValue")
for i in range(count + 1):
    print(sparse[i][0], "\t", sparse[i][1], "\t", sparse[i][2])