n = int(input())

def recursive1(n):
    if n == 0: return

    recursive1(n-1)
    print(n, end =' ')

def recursive2(n):
    if n == 0: return

    print(n, end =' ')
    recursive2(n-1)


recursive1(n)
print()
recursive2(n)
