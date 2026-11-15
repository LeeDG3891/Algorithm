y, m, d = map(int, input().split())

def leap_year(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def func(y, m, d):
    if m < 1 or m > 12 or d < 1:
        return -1

    if m == 2:
        if d > 28 + leap_year(y):
            return -1
    elif m in [4, 6, 9, 11]:
        if d > 30:
            return -1
    elif d > 31:
        return -1

    if m == 12 or m <= 2:
        return "Winter"
    elif m <= 5:
        return "Spring"
    elif m <= 8:
        return "Summer"
    else:
        return "Fall"

print(func(y, m, d))