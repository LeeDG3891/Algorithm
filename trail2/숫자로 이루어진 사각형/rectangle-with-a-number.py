n = int(input())

def func(n):
    num = 1

    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if num > 9: num = 1
            
            arr[i][j] = num
            num += 1

    for i in arr:
        print(*i)


func(n)