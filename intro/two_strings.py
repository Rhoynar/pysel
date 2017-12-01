str1 = input('Enter string 1: ')
str2 = input('Enter string 2: ')

if str1 in str2:
    print(str1 + ' is a substring of ' + str2)
else:
    print(str1 + ' is not a substring of ' + str2)
