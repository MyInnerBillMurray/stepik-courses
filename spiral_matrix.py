n = int(input())
matrix = [[0] * n for i in range(n)]

flag = 0

for j in range(n):
    flag += 1
    matrix[0][j] += flag

step = 0

for numbers in range(n**2 + 1):
    n -= 1
    for i in range(step, n):
        flag += 1
        matrix[i + 1][j] += flag

    for j in range(n, step, -1):
        flag += 1
        matrix[i + 1][j - 1] += flag

    for i in range(n, step + 1, -1):
        flag += 1
        matrix[i - 1][j - 1] += flag

    for j in range(step + 1, n):
        flag += 1
        matrix[i - 1][j] += flag

    step += 1

for elements in matrix:
    print(*elements)