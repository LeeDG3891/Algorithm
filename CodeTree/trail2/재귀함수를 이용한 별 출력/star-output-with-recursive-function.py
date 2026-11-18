n = int(input())

def recursive(n):
    for i in range(1, n+1):
        print('*' * i)


recursive(n)