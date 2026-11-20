n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


result = 0
for i in range(n):
    for j in range(n):
        count = 0

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if in_range(nx, ny) and grid[nx][ny] == 1:
                count += 1

        if count >= 3:
            result += 1

print(result)