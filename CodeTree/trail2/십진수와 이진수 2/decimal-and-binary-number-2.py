N = input()

num = 0

for i in range(len(N)):
    num = num * 2 + int(N[i])

temp = num * 17
arr = []
while temp > 0:
    arr.append(temp % 2)
    temp //= 2

print(*arr[::-1], sep = '')
