n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def func(a, b):
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            return "Yes"
    return "No"

print(func(a,b))