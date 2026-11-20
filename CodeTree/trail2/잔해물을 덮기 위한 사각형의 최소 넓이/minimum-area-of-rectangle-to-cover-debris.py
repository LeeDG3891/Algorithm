x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

offset = abs(min(min(x1), min(y1), min(x2), min(y2)))
arr = [[0] * 2001 for _ in range(2001)]

for i in range(x1[0] + offset, x2[0] + offset):
    for j in range(y1[0] + offset, y2[0] + offset):
        arr[i][j] = 1

for i in range(x1[1] + offset, x2[1] + offset):
    for j in range(y1[1] + offset, y2[1] + offset):
        arr[i][j] = 0

min_x, min_y = 2001, 2001
max_x, max_y = -2001, -2001

for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

if max_x < min_x:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))