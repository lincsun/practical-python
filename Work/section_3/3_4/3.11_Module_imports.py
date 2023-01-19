# Modules imports
#
# exercise 3.11
from fileparse import parse_csv


def pr_list(l: list):
    for item in l:
        print(item)


def module_imports():
    # help(fileparse)
    # dir(fileparse)

    with open('../../Data/portfolio.csv') as f:
        portfolio = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    pr_list(portfolio)
    print()

    with open('../../Data/prices.csv') as f:
        price_list = parse_csv(f, types=[str, float], has_header=False)
    pr_list(price_list)
    print()

    prices = dict(price_list)
    print(prices)

    print(prices['IBM'])


if __name__ == '__main__':
    module_imports()
