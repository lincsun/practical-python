# List of Dictionaries
#
# exercise 2.5

import report
from pprint import pprint


def list_of_dictionaries():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    pprint(portfolio)  # format output print, easier to read

    total = 0
    for i in range(len(portfolio)):
        total += portfolio[i]['shares'] * portfolio[i]['price']

    print('get total: {}'.format(total))


if __name__ == '__main__':
    list_of_dictionaries()
