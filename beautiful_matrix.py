# beautiful_matrix_simple.py

matrix = []

# 5 line input nibo
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# 1 er position khujbo
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row = i + 1   # 1-index
            col = j + 1

# center hocche (3,3)
moves = abs(row - 3) + abs(col - 3)

print(moves)