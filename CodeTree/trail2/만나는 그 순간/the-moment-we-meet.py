n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

total_time = sum(t)
arr = [0] * (total_time + 1)
arr2 = [0] * (total_time + 1)

now = 0
for i in range(n):
    for j in range(t[i]):
        now += 1

        if d[i] == 'R':
            arr[now] = arr[now - 1] + 1
        else:
            arr[now] = arr[now - 1] - 1

now = 0
for i in range(m):
    for j in range(t2[i]):
        now += 1

        if d2[i] == 'R':
            arr2[now] = arr2[now - 1] + 1
        else:
            arr2[now] = arr2[now - 1] - 1

for i in range(1, total_time + 1):
    if arr[i] == arr2[i]:
        print(i)
        break
else:
    print(-1)