# Making dictionaries
#
# exercise 2.25

import csv
from pprint import pprint


def making_dictionaries():
    with open('../../Data/portfolio.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)  # get headers

        types = [str, int, float]

        inst_dict = [dict(zip(headers, [func(val) for func, val in zip(types, row)])) for row in rows]
        pprint(inst_dict)


if __name__ == '__main__':
    making_dictionaries()
