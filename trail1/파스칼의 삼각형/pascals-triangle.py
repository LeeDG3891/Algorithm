n = int(input())

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if j < i:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        elif j == i:
            arr[i][j] = 1

for i in range(n):
    print(*arr[i][:i+1])