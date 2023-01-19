# fileparse.py
#
# Exercise 3.3
import csv
import gzip


def parse_csv(lines, select=None, types=None, has_header=True, delimiter=',', silence_errors=False) -> list:
    """
    Parse a CSV file into a list of records
    :param filename: the filename of csv file
    :return: a list of dictionaries
    """
    if select != None and has_header == False:
        raise RuntimeError(f'select:{select}, has_header: {has_header}')

    rows = csv.reader(lines, delimiter=delimiter)

    headers = next(rows) if has_header else []

    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    # print(indices, headers)
    records = []
    for idx, row in enumerate(rows, 1):
        if not row:
            continue

        if select:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {idx}: Couldn't convert {row}")
                    print(f"Row {idx}: Reason {e}")
                continue

        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records


if __name__ == '__main__':
    with open('../../Data/portfolio.csv') as f:
        records = parse_csv(f, select=['name'])
        print(records)

        f.seek(0)
        records = parse_csv(f, types=[str, int, float])
        print(records)

    with open('../../Data/prices.csv') as f:
        records = parse_csv(f, types=[str, float], has_header=False)
        print(records)

    with open('../../Data/portfolio.dat') as f:
        # rows = csv.reader(f)
        # for row in rows:
        #     for r in row:
        #         inst_list = [r.split(' ')]
        #         print(inst_list)
        #     print(row, row.__class__)
        records = parse_csv(f, types=[str, int, float], delimiter=' ')
        print(records)

    with gzip.open('../../Data/portfolio.csv.gz', 'rt') as file:
        records = parse_csv(file, types=[str, int, float])
        print(records)
