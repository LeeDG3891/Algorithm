a, b = map(int, input().split())

def func(a, b):
    result = 1
    
    for i in range(b):
        result *= a

    return result

print(func(a, b))