n, t = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
result = 0
for i in range(n):
    if arr[i] > t:
        count += 1
    else:
        count = 0

    result = max(result, count)

print(result)