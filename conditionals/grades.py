

# Scale:
# 9-10 - A
# 7-8  - B
# 5-6  - B-
# 3-4  - C
# 0-2  - D

score = int(input('Enter your score between 1..10: '))
if (score <= 2):
    print('Grade D')
elif (score <= 4):
    print('Grade C')
elif (score <= 6):
    print('Grade B-')
elif (score <= 8):
    print('Grade B')
else:
    print('Grade A')

