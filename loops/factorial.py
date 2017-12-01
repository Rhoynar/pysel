num = int(input('Enter a number to find factorial for: '))

if num > 15:
    print('number too big, enter a smaller number (<15) to find factorial')
elif num < 0:
    print('number is negative, factorial cannot be found.')
else:
    print('The factorial of this number is: ')
    product = 1
    while(num >= 1):
        product = product * num
        num = num - 1
    print(product)

