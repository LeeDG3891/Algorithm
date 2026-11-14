a, b = map(int, input().split())
count = 0

def func(i):
    return func2(i) or i % 3 == 0

def func2(i):
    if i == 0:
        return False
    return i % 10 in (3, 6, 9) or func2(i // 10)
    

for i in range(a, b+1):
    if func(i):
        count += 1

print(count)
