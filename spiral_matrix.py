n = int(input())
matrix = [[0] * n for i in range(n)]

flag = 0

for j in range(n):
    flag += 1
    matrix[0][j] += flag

s1 = 0
s3 = 0

for numbers in range(n**2 + 1):
    n -= 1
    for i in range(s1, n):
        flag += 1
        matrix[i + 1][j] += flag

    for j in range(n, s3, -1):
        flag += 1
        matrix[i + 1][j - 1] += flag

    for i in range(n, s3 + 1, -1):
        flag += 1
        matrix[i - 1][j - 1] += flag

    for j in range(s1 + 1, n):
        flag += 1
        matrix[i - 1][j] += flag

    s1 += 1
    s3 += 1

for elements in matrix:
    print(*elements)