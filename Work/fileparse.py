# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename: str, select=None, types=None, has_header=True, delimiter=',') -> list:
    """
    Parse a CSV file into a list of records
    :param filename: the filename of csv file
    :return: a list of dictionaries
    """
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        indices = []
        if has_header:
            headers = list(next(rows))
            indices = [i for i, h in enumerate(headers) if select == None or h in select]
        else:
            headers = []
        # print(indices)

        records = []
        for row in rows:
            if not row:
                continue

            if len(headers) != 0:
                real_headers = [headers[i] for i in indices]

                if types == None:
                    real_vals = [row[i] for i in indices]
                    record = dict(zip(real_headers, real_vals))
                else:
                    real_vals = zip(types, [row[i] for i in indices])
                    record = dict(zip(real_headers, [func(val) for func, val in real_vals]))
            else:
                try:
                    record = tuple([t(row[i]) for i, t in enumerate(types)])
                    # print(record, record.__class__)
                except:
                    print('except!')
                    continue

            records.append(record)

    return records


if __name__ == '__main__':
    records = parse_csv('Data/portfolio.csv', select=['name'])
    print(records)
    records = parse_csv('Data/portfolio.csv', types=[str, int, float])
    print(records)
    records = parse_csv('Data/prices.csv', types=[str, float], has_header=False)
    print(records)
    records = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
    print(records)
