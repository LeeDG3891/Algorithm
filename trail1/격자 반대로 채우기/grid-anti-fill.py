n = int(input())

arr = [[0] * n for _ in range(n)]
num = 1

for i in range(n-1, -1, -1):
    if (n - i - 1) % 2 == 0:
        for j in range(n-1, -1, -1):
            arr[j][i] = num
            num += 1
    else:
        for j in range(n):
            arr[j][i] = num
            num += 1

for i in arr:
    print(*i)