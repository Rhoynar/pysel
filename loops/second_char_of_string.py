
sentence = 'This is a long sentence with lots of words'

# Print every alternate character of the string.
for idx in range(0, len(sentence), 2):
    print(sentence[idx])

# Count the number of letter 'i' in the string.
count = 0
for ch in sentence:
    if ch == 'i':
        count += 1

print('Number of i in the string is: ' + str(count))

# Reverse a string.
print('--------------------------------------------')
for idx in range(len(sentence)-1, 0, -1):
    print(sentence[idx], end='')

print('')
