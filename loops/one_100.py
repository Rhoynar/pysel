# Print 1.. 100 in vertical rows.

for i in range(1,11):
    for j in range(10):
        print(str(j*10+i) + '\t', end='')
    print('')

