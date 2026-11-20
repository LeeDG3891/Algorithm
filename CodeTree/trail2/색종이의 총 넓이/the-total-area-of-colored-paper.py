n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

offset = abs(min(min(x), min(y)))
arr = [[0] * 201 for _ in range(201)]

for k in range(n):
    for i in range(x[k] + offset, x[k] + offset + 8):
        for j in range(y[k] + offset, y[k] + offset + 8):
            arr[i][j] = 1

count = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 1:
            count += 1

print(count)