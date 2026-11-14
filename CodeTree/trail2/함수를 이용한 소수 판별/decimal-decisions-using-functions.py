a, b = map(int, input().split())

def func(n, m):
    result = 0

    for i in range(n, m+1):
        for j in range(2, i):
            if i % j == 0:
                break
        
        else: result += i
            
    return result

print(func(a, b))