M, D = map(int, input().split())

def func(a, b):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if 1 <= a <= 12 and 1 <= b <= days[a-1]:
        return "Yes"
    else:
        return "No"

print(func(M, D))