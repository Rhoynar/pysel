# An example of function calling another
def func_a():
    print('A')


# func_b() calls system function print()
def func_b():
    print('B')


# func_ab() calls func_a() and func_b()
def func_ab():
    func_a()
    func_b()
    print('Done!')


# Main calls func_ab()
def main():
    func_ab()


# Call main() function.
main()