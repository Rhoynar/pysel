orig_num = int(input('Enter a number: '))

num = orig_num

if num < 0:
    num = (-1) * num

sum_of_digits = 0
while (num > 0):
    digit = num % 10
    sum_of_digits += digit
    num = int(num/10)

print('Sum of digits of ' + str(orig_num) + ' is: ' + str(sum_of_digits))

