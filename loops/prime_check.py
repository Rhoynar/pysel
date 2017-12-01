# Check if a number is prime
num = int(raw_input('Enter number: '))

prime = True
for i in range(2, int(num/2)):
    if num % i == 0:
        prime = False
        break

if prime:
    print('Number {} is a prime number!'.format(num))
else:
    print('Number {} is NOT a prime number!'.format(num))
