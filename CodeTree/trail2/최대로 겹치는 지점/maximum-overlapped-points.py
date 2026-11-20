n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

arr = [0] * 101

for a, b in segments:
    for i in range(a, b+1):
        arr[i] += 1

result = 0

for i in range(len(arr)):
    result = max(result, arr[i])

print(result)