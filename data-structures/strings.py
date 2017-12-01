# program to replace {} with user provided input.

# Ex:
# Today is {} and it is a happy day!  <-  Monday, Tuesday, wednesday etc.

inp_str = input('Enter a string with {}: ')
inp_repl = input('Enter a replacement variable: ' )


index = inp_str.find('{}')
if index >= 0:
    ret_str = inp_str[:index] + inp_repl + inp_str[index+2:]
    print(ret_str)
else:
    print('{} is not found!')
