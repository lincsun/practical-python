# A list of tuples
#
# exercise 2.4

import report
import stock


def a_list_of_tuples():
    with open('../../Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    total = 0
    p: stock.Stock
    for p in portfolio:
        # print('index_{} of list: {}'.format(i, portfolio[i]))
        total += (int(p.shares) * float(p.price))

    print('use 2-D array type: get total: {}'.format(total))

    total = 0
    p: stock.Stock
    for p in portfolio:
        # print('index_{} of list: {}'.format(i, portfolio[i]))
        name, shares, price = p.name, p.shares, p.price
        total += (shares * price)

    print('use single object type: get total: {}'.format(total))


if __name__ == '__main__':
    a_list_of_tuples()
