m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
result1 = d1
result2 = d2

for i in range(m1):
    result1 += num_of_days[i]

for i in range(m2):
    result2 += num_of_days[i]

print(result2 - result1 + 1)