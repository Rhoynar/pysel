numbers = [-4, 4, 12, 83, -88, 77, 27]

min_num = None
max_num = None

for idx in range(len(numbers)):
    num = numbers[idx]
    if min_num is None or min_num > num:
        min_num = num

    if max_num is None or max_num < num:
        max_num = num

print('Min: ' + str(min_num))
print('Max: ' + str(max_num))




