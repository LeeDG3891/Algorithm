n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0

for i in range(n):
    for j in range(n - 2):
        count = grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
        result = max(result, count)

print(result)