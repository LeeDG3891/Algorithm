import sys

n = int(input())
A = list(map(int, input().split()))

result = sys.maxsize

for i in range(n):
    total = 0

    for j in range(n):
        total += abs(i - j) * A[j]

    result = min(result, total)

print(result)