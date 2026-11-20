N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

count = [0] * (N + 1)
result = -1

for i in range(M):
    count[student[i]] += 1

    if count[student[i]] >= K:
        result = student[i]
        break

print(result)