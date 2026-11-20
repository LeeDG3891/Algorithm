n = int(input())
arr = [int(input()) for _ in range(n)]

count = 0
result = 0
for i in range(n):
    if i == 0 or arr[i] > arr[i-1]:
        count += 1
    else:
        count = 1

    result = max(result, count)

print(result)