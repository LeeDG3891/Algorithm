arr = [list(map(int, input().split())) for _ in range(2)]


for i in range(len(arr)):
    print(f"{sum(arr[i]) / len(arr[i]):.1f}", end=" ")
print()

for j in range(len(arr[0])):
    print(f"{(arr[0][j] + arr[1][j]) / len(arr):.1f}", end=" ")
print()

total = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        total += arr[i][j]

print(f"{total / (len(arr) * len(arr[0])):.1f}")