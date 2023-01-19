# More on Functions
#
# exercise 3.2.0

global_val = 3


def test_func(val, debug=False):
    """
    test func: print 'Hello World'
    :return: none
    """
    if debug:
        print('Hello World! debug mode!')
        val = 4  # common variable is not mutable
    else:
        print('Hello World! normal mode!')

    return val, 2


def scripting():
    test_func(1)  # default no debug mode

    val = 3
    x = a, b = test_func(val, debug=True)  # debug mode
    print(a, b, x, x.__class__, val)

    global global_val  # declare global_val is a global variable, or received error
    print('global_val: {}'.format(global_val))
    global_val = 4
    print('global_val--after modified: {}'.format(global_val))


if __name__ == '__main__':
    scripting()
