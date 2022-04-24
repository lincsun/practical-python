# Containers
#
# exercise 2.2.0


def container_test():
    records = []
    with open('Data/portfolio.csv', 'rt') as f:
        next(f)
        for line in f:
            # print('get line: {}, class: {}'.format(line, line.__class__))
            row = line.split(',')

            records.append((row[0], int(row[1]), float(row[2])))

        print('get records: {}'.format(records))

    prices = {
        'GOOG': 513.25,
        'CAT': 87.22,
        'IBM': 93.37,
        'MSFT': 44.12
    }
    print('get prices: {}, class: {}'.format(prices, prices.__class__))

    print(prices['IBM'], prices['GOOG'])
    del prices

    prices = {'GOOG': 513.25, 'CAT': 87.22, 'IBM': 93.37}

    print('get new prices: {}, class: {}'.format(prices, prices.__class__))

    prices = {}  # Initial empty dict

    with open('Data/prices.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            prices[row[0]] = float(row[1])


'''
    inst_list_by_tuple = []
    with open('Data/prices.csv', 'rt') as f:
        for line in f:
            row = line.split(',')
            print(type(row), row)
            #            print(row[0], row[0].__class__, float(row[1]), float(row[1]).__class__)
            inst_str = row[0]
            inst_float = float(row[1])
            t = (inst_str, inst_float)
            print(type(t))
            inst_list_by_tuple.append(t)
            # inst_list_by_tuple.

    inst_dict = dict(inst_list_by_tuple)
    print('get dict from prices.csv: {}'.format(inst_dict))
'''

if __name__ == '__main__':
    container_test()
