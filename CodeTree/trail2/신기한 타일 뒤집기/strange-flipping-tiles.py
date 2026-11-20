n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

arr = [0] * 2000001
now = 1000000

for i in range(n):
    if dir[i] == 'R':
        for j in range(now, now + x[i]):
            arr[j] = 1
        now += x[i] -1
    else:
        for j in range(now, now - x[i], -1):
            arr[j] = 2
        now -= x[i] -1

countr = 0
countl = 0
for i in range(len(arr)):
    if arr[i] == 1:
        countr += 1
    elif arr[i] == 2:
        countl += 1

print(countl, countr)