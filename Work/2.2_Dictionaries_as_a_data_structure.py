# Dictionaries as a data structure
#
# exercise 2.2

import csv


def dictionary_test():
    f = open('Data/portfolio.csv')
    rows = csv.reader(f)

    # name, shares, price
    print('labels: {}'.format(next(rows)))

    row = next(rows)
    print('get line: {}'.format(row))

    t = (row[0], int(row[1]), float(row[2]))
    print('get tuple: {}, class: {}'.format(t, t.__class__))

    d = {
        'name': row[0],
        'shares': int(row[1]),
        'price': float(row[2])
    }
    print('get dict: {}'.format(d))

    cost = d['shares'] * d['price']
    print('cost: {}'.format(cost))

    d['shares'] = 75
    print('new dict: {}'.format(d))

    d['date'] = '4/24/2022'
    d['account'] = 12345
    print('new new dict: {}'.format(d))

    f.close()


if __name__ == '__main__':
    dictionary_test()
