# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print('headers: {}'.format(headers))

        total = 0
        for n, row in enumerate(rows, start=1):
            records = dict(zip(headers, row))
            try:
                shares = int(records['shares'])
                price = float(records['price'])
                total += shares * price
            except:
                print('Row {}: Bad row: {}'.format(n, row))

        print('Total cost {}'.format(total))
