# A list of tuples
#
# exercise 2.4

import report


def a_list_of_tuples():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    print('{}: get list {}'.format(__name__, portfolio))

    total = 0
    for i in range(len(portfolio)):
        # print('index_{} of list: {}'.format(i, portfolio[i]))
        total += (portfolio[i][1] * portfolio[i][2])

    print('use 2-D array type: get total: {}'.format(total))

    total = 0
    for i in range(len(portfolio)):
        # print('index_{} of list: {}'.format(i, portfolio[i]))
        name, shares, price = portfolio[i]
        total += (shares * price)

    print('use single object type: get total: {}'.format(total))


if __name__ == '__main__':
    a_list_of_tuples()
