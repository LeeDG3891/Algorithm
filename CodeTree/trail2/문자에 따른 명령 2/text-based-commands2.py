dirs = input()

x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
d = 3

for dir in dirs:
    if dir == 'L':
        d = (d - 1 + 4) % 4
    elif dir == 'R':
        d = (d + 1) % 4
    else:
        x += dx[d]
        y += dy[d]

print(x, y)