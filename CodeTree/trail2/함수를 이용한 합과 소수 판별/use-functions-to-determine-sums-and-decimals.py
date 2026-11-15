a, b = map(int, input().split())

def func(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def func2(a):
    return ((a // 10) + (a % 10)) % 2 == 0

count = 0
for i in range(a, b+1):
    if func(i) and func2(i):
        count += 1

print(count)