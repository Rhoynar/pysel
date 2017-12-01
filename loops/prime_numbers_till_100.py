
# Numbers between 1..100 that are primes.
for i in range(2, 100):

    # Check if i is prime.
    i_is_prime = True
    for j in range(2, i):
        if i % j == 0:
            i_is_prime = False
            break

    # If i is prime, print i
    if i_is_prime == True:
        print(i)
