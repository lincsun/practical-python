# First-class Data
#
# exercise 2.24

import csv
from pprint import pprint


def first_class_data():
    with open('../../Data/portfolio.csv') as f:
        types = [str, int, float]

        rows = csv.reader(f)
        next(rows)  # skip labels

        inst_list = [list(zip(types, row)) for row in rows]
        pprint(inst_list)

        portfolio = [[func(val) for func, val in l] for l in inst_list]
        pprint(portfolio)


if __name__ == '__main__':
    first_class_data()
