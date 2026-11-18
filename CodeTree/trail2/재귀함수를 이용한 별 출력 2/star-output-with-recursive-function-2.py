n = int(input())

def recursive(n, i):
    if i > n:
        return

    print("* " * (n - i + 1), sep = ' ')
    recursive(n, i+1)
    print("* " * (n - i + 1), sep = ' ')


recursive(n, 1)