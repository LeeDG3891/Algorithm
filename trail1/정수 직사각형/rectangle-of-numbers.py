n, m = map(int, input().split())

arr = [[i * m + j + 1 for j in range(m)] for i in range(n)]

for row in arr:
    print(*row)