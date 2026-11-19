n = int(input())
arr = []

if n == 0:
    arr.append(0)

while n > 0:    
    arr.append(n % 2)
    n //= 2

print(*arr[::-1], sep='')