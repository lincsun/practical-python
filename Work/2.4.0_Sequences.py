# Sequences
#
# exercise 2.4.0

import report


def sequences():
    portfilio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    inst_list = report.make_report(portfilio, prices)
    for i, r in enumerate(inst_list, start=1):
        print(i, r[0], r[1], round(r[2], 2), round(r[3], 2))

    columns = ['name', 'shares', 'price']
    values = ['GOOG', 100, 490.1]
    pairs = zip(columns, values)

    # print(list(pairs), pairs.__class__)
    print(dict(pairs))
    return


if __name__ == '__main__':
    sequences()
