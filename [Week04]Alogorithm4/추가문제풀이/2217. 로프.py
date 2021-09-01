import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
max_weight = nums[-1]
product_cnt = n

for i in range(n):
    max_weight = max(nums[i] * product_cnt, max_weight)
    product_cnt -= 1
    
print(max_weight)
