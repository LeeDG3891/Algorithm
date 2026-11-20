A = input()
n = len(A)

result = 0

for i in range(n):
    for j in range(i + 1, n):
        if A[i] == '(' and A[j] == ')':
            result += 1

print(result)