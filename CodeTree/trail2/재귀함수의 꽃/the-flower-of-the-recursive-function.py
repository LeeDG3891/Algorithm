N = int(input())

def recursive(n, i):
    if i > n:
        return

    print(n - i + 1, end = ' ')
    recursive(n, i+1)
    print(n - i + 1, end = ' ')


recursive(N, 1)