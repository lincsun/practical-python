# Modules imports
#
# exercise 3.11
from fileparse import parse_csv


def module_imports():
    # help(fileparse)
    # dir(fileparse)

    portfolio = parse_csv('Data/portfolio.csv', select=['name', 'shares', 'price'], types=[str, int, float])
    print(portfolio)

    price_list = parse_csv('Data/prices.csv', types=[str, float], has_header=False)
    print(price_list)

    prices = dict(price_list)
    print(prices)

    print(prices['IBM'])


if __name__ == '__main__':
    module_imports()
