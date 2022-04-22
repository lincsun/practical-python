# pcost.py
#
# Exercise 1.27

import csv


def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print('headers: {}'.format(headers))

        total = 0
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except:
                print('invalid value!')

        print('Total cost {}'.format(total))
