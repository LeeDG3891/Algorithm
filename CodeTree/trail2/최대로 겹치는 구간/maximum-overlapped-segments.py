n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

offset = abs(min(min(a, b) for a, b in segments))
arr = [0] * 201

for a, b in segments:
    a += offset
    b += offset

    for i in range(a-1, b-1):
        arr[i] += 1

result = 0
for i in range(len(arr)):
    result = max(result, arr[i])

print(result)