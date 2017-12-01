num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))

if num1 > num2 and num1 > num3:
    print(str(num1) + ' is the greatest!')

if num2 > num3 and num2 > num1:
    print(str(num2) + ' is the greatest!')

if num3 > num1 and num3 > num2:
    print(str(num3) + ' is the greatest!')
