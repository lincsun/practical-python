# The Big Picture
#
# exercise 2.26

import csv


def the_big_picture():
    f = open('Data/dowstocks.csv')
    rows = csv.reader(f)
    headers = next(rows)
    row = next(rows)

    print(headers, row)

    types = [str, float, str, str, float, float, float, float, int]
    converted = [func(val) for func, val in zip(types, row)]
    record = dict(zip(headers, converted))

    print(record, record['name'])

    # convert date into tuple
    inst_tuple = tuple(int(i) for i in record['date'].split('/'))
    print(inst_tuple)

    f.close()


if __name__ == '__main__':
    the_big_picture()
