# Datatypes and Data structures
#
# exercise 2.1.0

import csv


def datatypes_test():
    inst_tuple_0 = ('GOOG', 100, 490.1)
    print(inst_tuple_0, inst_tuple_0.__class__)

    inst_tuple_0 = (inst_tuple_0[0], 100, inst_tuple_0[2])
    print(inst_tuple_0, inst_tuple_0.__class__)

    f = open('Data/portfolio.csv')
    rows = csv.reader(f)
    print('get rows: {}'.format(rows))
    print('labels: {}'.format(next(rows)))

    row = next(rows)
    print('next row: {}, index_1: {}, index_2: {}'.format(row, row[1].__class__, row[2]))

    cost = int(row[1]) * float(row[2])
    print('cost: {}'.format(round(cost, 2)))


if __name__ == '__main__':
    datatypes_test()
