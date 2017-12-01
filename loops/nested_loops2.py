# Print numbers 1.. 100 in rows of 10.

count = 1
for i in range(10):
    for j in range(10):
        print(str(count) + '\t', end='')
        count += 1
    print('')

# Print numbers 1..10 using single loop
for idx in range(1, 101):
    print(str(idx) + '\t', end='')
    if idx % 10 == 0:
        print('')


