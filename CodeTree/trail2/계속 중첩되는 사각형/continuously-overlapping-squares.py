n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

offset = abs(min(min(x1), min(y1), min(x2), min(y2)))
arr = [[0] * 201 for _ in range(201)]

for k in range(n):
    for i in range(x1[k] + offset, x2[k] + offset):
        for j in range(y1[k] + offset, y2[k] + offset):
            if k % 2 == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = 2

count = 0
for i in range(201):
    for j in range(201):
        if arr[i][j] == 2:
            count += 1

print(count)