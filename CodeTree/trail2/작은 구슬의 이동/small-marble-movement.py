n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

if d == 'U':
    dir = 0
elif d == 'R':
    dir = 1
elif d == 'D':
    dir = 2
else:
    dir = 3

for i in range(t):
    nx = r + dx[dir]
    ny = c + dy[dir]

    if in_range(nx, ny):
        r, c = nx, ny
    else:
        dir = (dir + 2) % 4

print(r, c)