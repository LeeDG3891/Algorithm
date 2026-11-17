n = int(input())
arr = list(map(int, input().split()))

def func(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2

func(arr)
print(*arr)