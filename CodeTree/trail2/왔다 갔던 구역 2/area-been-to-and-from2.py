n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

arr = [0] * 20001
now = 10000

for i in range(n):
    if dir[i] == 'R':
        for j in range(now, now + x[i]):
            arr[j] += 1
        now += x[i]
    else:
        for j in range(now-1, now - x[i] - 1, -1):
            arr[j] += 1
        now -= x[i]

result = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        result += 1

print(result)