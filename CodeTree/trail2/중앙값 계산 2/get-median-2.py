n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        arr[:i+1] = sorted(arr[:i+1])
        print(arr[i // 2], end=' ')
