# Sequences
#
# exercise 2.4.0

import report


def sequences():
    with open('Data/portfolio.csv') as f:
        portfilio = report.read_portfolio(f)
    with open('Data/prices.csv') as f:
        prices = report.read_prices(f)

    inst_list = report.make_report(portfilio, prices)
    report.print_report(inst_list)

    columns = ['name', 'shares', 'price']
    values = ['GOOG', 100, 490.1]
    pairs = zip(columns, values)

    # print(list(pairs), pairs.__class__)
    print(dict(pairs))
    return


if __name__ == '__main__':
    sequences()
