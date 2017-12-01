# Print numbers that are divisible by 5 but not by 3
# Examples: 5, 10, 20, 25, 35, 40, 50 ..

for i in range(1, 21):
    if i*5 % 3 == 0:
        pass
    else:
        print(i*5)

print('------------------------------------')
for i in range(1, 21):
    if i*5 % 3 == 0:
        continue

    print(i*5)
