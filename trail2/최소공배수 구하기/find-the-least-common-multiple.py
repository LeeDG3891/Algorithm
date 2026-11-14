n, m = map(int, input().split())

def lcm(n, m):
    x, y = n, m
    while y != 0:
        x, y = y, x % y

    print((n * m) // x)

lcm(n, m)