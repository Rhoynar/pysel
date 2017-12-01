# When user enters 'exit', exit program
while (True):
    inp = raw_input('> ')
    if inp.lower() == 'exit':
        break
    else:
        print(inp)
