n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]

for i in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = i + 1

for i in arr:
    print(*i)