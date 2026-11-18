n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

arr = []

for word in str:
    if word[:len(t)] == t:
        arr.append(word)

arr.sort()
print(arr[k-1])