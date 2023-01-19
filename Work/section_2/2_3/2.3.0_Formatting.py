# Formatting
#
# exercise 2.3.0

from pprint import pprint


def formatting_test():
    name = 'IBM'
    shares = 100
    price = 91.1

    print(name, shares, price)
    print(f'{name:>10s} {shares:>10d} {price:>10.2f}')

    s = {
        'name': 'IBM',
        'shares': 100,
        'price': 91.1
    }
    print(s)
    print('names: {:>10s}, shares: {:10d}, price: {:10.2f}'.format(s.get('name'), s.get('shares'), s.get('price')))
    pprint(s)  # sort elements of dictionary by character


if __name__ == '__main__':
    formatting_test()
