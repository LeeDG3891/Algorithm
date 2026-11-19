a, b, c = map(int, input().split())

if (a, b, c) < (11, 11, 11):
    print(-1)
else:
    print(((a - 11) * 24 * 60) + ((b - 11) * 60) + (c - 11))