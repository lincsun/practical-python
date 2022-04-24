# Dictionaries as a container
#
# exercise 2.6

import report


def dictionaries_as_a_container():
    prices = {'IBM': 92.45, 'MSFT': 45.12}
    print('get prices: {}'.format(prices))

    # error, cause no key 'AAPL' in dict
    # print('get price of AAPL: {}'.format(prices['AAPL']))

    print('if key \'AAPL\' in prices: {}'.format('AAPL' in prices))

    price_dict = report.read_prices('Data/prices.csv')
    print('get dict: {}, class: {}'.format(price_dict, price_dict.__class__))

    print(price_dict['IBM'], price_dict['MSFT'])


if __name__ == '__main__':
    dictionaries_as_a_container()
