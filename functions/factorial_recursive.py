# A recursive function example
# Find factorial of a number

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# Call the function:
num = int(input('Enter a number to find factorial: '))
print(str(num) + ' != ' + str(factorial(num)))
