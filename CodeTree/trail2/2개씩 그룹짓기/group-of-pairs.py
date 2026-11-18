n = int(input())
nums = list(map(int, input().split()))

nums.sort()

result = 0

for i in range(n):
    total = nums[i] + nums[2 * n - 1 - i]
    result = max(result, total)

print(result)