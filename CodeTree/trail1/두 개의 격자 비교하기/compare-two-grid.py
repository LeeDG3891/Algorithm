n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

new = []

for i in range(n):
    row = []
    for j in range(m):
        if arr1[i][j] == arr2[i][j]: row.append(0)
        else: row.append(1)
    new.append(row)

for row in new:
    print(*row)