A = input()

def func(str):
    for i in range(len(str)):
        for j in range(len(str)):
            if str[i] != str[j]:
                return print("Yes")
    else:
        return print("No")

func(A)