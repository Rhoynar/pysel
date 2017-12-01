nums = [4, 1, 5, 2, 3, 6, 5, 4, 2]
print(nums)

results = []

while (len(nums) > 0):

    min_num = None
    for num in nums:
        if min_num is None or min_num > num:
            min_num = num

    results.append(min_num)
    nums.remove(min_num)

print(results)