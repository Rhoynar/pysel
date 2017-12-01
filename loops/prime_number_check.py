import math

num = int(input('Enter number: '))

prime = True
for i in range(2, int(math.sqrt(num))):
    if num % i == 0:
        prime = False
        break

if prime is True:
    print('Number: ' + str(num) + ' is a prime number')
else:
    print('Number: ' + str(num) + ' is not a prime number')
