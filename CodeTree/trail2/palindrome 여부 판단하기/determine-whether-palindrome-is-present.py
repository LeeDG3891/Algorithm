A = input()

def func(str):
    str = str[::-1]
    return str

if A == func(A):
    print("Yes")
else:
    print("No")