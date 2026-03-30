import sys
input = sys.stdin.readline

arr = [0] * 43
count = 0

for _ in range(10):
    n = int(input()) % 42
    
    if (arr[n] == 0):
        arr[n] = 1
        count += 1

print(count)