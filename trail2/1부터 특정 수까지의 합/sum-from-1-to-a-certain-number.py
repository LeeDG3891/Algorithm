n = int(input())

def func(n):
    num = 0
    for i in range(1, n+1):
        num += i

    return num // 10

print(func(n))