# Some additional dictionary operations
#
# exercise 2.3

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

    # convert dictionary into list
    l = list(d)
    print('get: {}, class:{}'.format(l, l.__class__))

    for k in d:
        print(k, 'k=', d[k])

    keys = d.keys()
    print('keys: {}'.format(keys))

    for k in keys:
        print('value: {}'.format(d[k]))

    # keys is dynamically updated
    del d['account']
    print('after del key \'account\', get: {}'.format(keys))

    items = d.items()
    print('items: {}, class: {}'.format(items, items.__class__))

    for k, v in items:
        print(k, '=', v)

    # convert list of tuples into dictionary
    print('we have items: {}'.format(items))

    inst_dict = dict(items)
    print('after dict, we get: {}'.format(inst_dict))

    f.close()


if __name__ == '__main__':
    dictionary_test()
