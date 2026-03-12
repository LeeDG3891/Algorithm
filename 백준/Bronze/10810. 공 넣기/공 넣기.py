import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] * n

for _ in range(m):
  i, j, k = map(int, input().split())

  for idx in range(i-1, j):
    arr[idx] = k

print(*arr)
