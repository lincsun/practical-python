# List of Dictionaries
#
# exercise 2.5

import report
from pprint import pprint
import stock


def list_of_dictionaries():
    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)
    # pprint(portfolio)  # format output print, easier to read

    total = 0
    p: stock.Stock
    for p in portfolio:
        total += int(p.shares) * float(p.price)

    print('get total: {}'.format(total))


if __name__ == '__main__':
    list_of_dictionaries()
