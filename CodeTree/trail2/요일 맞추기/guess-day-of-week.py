m1, d1, m2, d2 = map(int, input().split())

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

result1 = d1
result2 = d2

for i in range(m1-1):
    result1 += num_of_days[i]

for i in range(m2-1):
    result2 += num_of_days[i]

if (result2 - result1) % 7 == 0:
    print("Mon")
elif (result2 - result1) % 7 == 1:
    print("Tue")
elif (result2 - result1) % 7 == 2:
    print("Wed")
elif (result2 - result1) % 7 == 3:
    print("Thu")
elif (result2 - result1) % 7 == 4:
    print("Fri")
elif (result2 - result1) % 7 == 5:
    print("Sat")
else:
    print("Sun")