# f-strings
#
# exercise 1.17

def f_string_test():
    name = 'ALIBABA'
    shares = 100
    price = 91.1

    print(f'{shares:3d} shares of {name:>10s} at ${price:0.2f}')


if __name__ == '__main__':
    f_string_test()
