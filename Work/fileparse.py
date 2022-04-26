# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename: str, select=None, types=None, has_header=True, delimiter=',', silence_errors=False) -> list:
    """
    Parse a CSV file into a list of records
    :param filename: the filename of csv file
    :return: a list of dictionaries
    """
    if select != None and has_header == False:
        raise RuntimeError(f'select:{select}, has_header: {has_header}')

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
        for idx, row in enumerate(rows, start=1):
            if not row:
                continue

            record = {}
            try:
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
                        record = tuple(func(val) for func, val in zip(types, row))
                        # print(record, record.__class__)
                    except:
                        if not silence_errors:
                            print('except!')
                        continue

                records.append(record)

            except:
                if not silence_errors:
                    print('Row{}: Couldn\'t convert {}'.format(idx, row))
                continue

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
