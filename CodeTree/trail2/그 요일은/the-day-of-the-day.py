m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

result1 = d1
result2 = d2

for i in range(m1-1):
    result1 += num_of_days[i]

for i in range(m2-1):
    result2 += num_of_days[i]

diff = result2 - result1
count = 0

for i in range(diff + 1):
    if days[i % 7] == A:
        count += 1

print(count)