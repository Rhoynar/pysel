# Print all prime numbers between 2..100
for i in range(2, 100):

    i_is_prime = True
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            i_is_prime = False
            break

    if i_is_prime:
        print(i)