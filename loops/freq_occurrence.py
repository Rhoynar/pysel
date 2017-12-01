# Find freq of occurrence of each number:
nums = [1, 1, 3, 4, 2, 1, 2, 3, 2, 5, 6, 3, 2, 1, 1, 2, 3, 4, 2]

# Answer:
# 1: 5
# 3: 4
# 4: 2
# 2: 6

done = []

for i in range(len(nums)):
    num = nums[i]

    count_num = 0
    if num not in done:
        for j in range(len(nums)):
            if nums[j] == num:
                count_num +=1

        done.append(num)
        print('i: {}, count: {}'.format(num, count_num))

#######  ########

done = []
for num in nums:
    if num not in done:
        print(nums.count(num))
        done.append(num)
