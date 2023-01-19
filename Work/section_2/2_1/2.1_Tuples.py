# Tuples
#
# exercise 2.1

import csv


def tuple_test():
    f = open('../../Data/portfolio.csv')
    rows = csv.reader(f)

    # name, shares, price
    print('labels: {}'.format(next(rows)))

    row = next(rows)
    print('get line: {}'.format(row))

    t = (row[0], int(row[1]), float(row[2]))
    print('get tuple: {}, class: {}'.format(t, t.__class__))

    cost = t[1] * t[2]
    print('cost: {}'.format(round(cost, 2)))

    t = (t[0], 75, t[2])
    print('new t: {}'.format(t))

    name, shares, price = t
    print(name, shares, price)

    t = (name, 2 * shares, price)
    print('new new t: {}'.format(t))

    f.close()


if __name__ == '__main__':
    tuple_test()
