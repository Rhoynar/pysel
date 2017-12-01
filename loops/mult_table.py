# Print multiplication tables


# 1     2       3       4       ..          10
# 2     4       6       8                   20
# 3     6       9       12                  30
# ..    ..      ..      ..                  ..


for i in range(1, 11):
    for j in range(1, 11):
        print(str(j * i) + '\t', end='')
    print('')
