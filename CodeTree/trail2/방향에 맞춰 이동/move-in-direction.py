n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

x, y = 0, 0

for i in range(n):
    if dir[i] == 'E':
        d = 0
    elif dir[i] == 'W':
        d = 1
    elif dir[i] == 'S':
        d = 3
    else:
        d = 2

    x += dx[d] * dist[i]
    y += dy[d] * dist[i]

print(x, y)