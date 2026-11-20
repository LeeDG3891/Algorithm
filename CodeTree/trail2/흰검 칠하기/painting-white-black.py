n = int(input())
commands = [tuple(input().split()) for _ in range(n)]

x = []
dir = []

for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

arr = [0] * 200001
black = [0] * 200001
white = [0] * 200001

now = 100000

for i in range(n):
    if dir[i] == 'R':
        for j in range(now, now + x[i]):
            if arr[j] == 2:
                continue

            black[j] += 1

            if black[j] >= 2 and white[j] >= 2:
                arr[j] = 2
            else:
                arr[j] = 1

        now += x[i] - 1

    else:
        for j in range(now, now - x[i], -1):
            if arr[j] == 2:
                continue

            white[j] += 1

            if black[j] >= 2 and white[j] >= 2:
                arr[j] = 2
            else:
                arr[j] = -1

        now -= x[i] - 1

count1 = 0
count2 = 0
count3 = 0

for i in range(len(arr)):
    if arr[i] == 1:
        count1 += 1
    elif arr[i] == -1:
        count2 += 1
    elif arr[i] == 2:
        count3 += 1

print(count2, count1, count3)
