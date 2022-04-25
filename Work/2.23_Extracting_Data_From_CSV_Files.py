# Extracting Data From CSV Files
#
# exercise 2.23

import csv
from pprint import pprint


def extracting_data_from_csv_files():
    f = open('Data/portfoliodate.csv')
    rows = csv.reader(f)
    headers = next(rows)
    print(headers)

    select = ['name', 'shares', 'price']
    indices = [headers.index(column_name) for column_name in select]
    print(indices)

    row = next(rows)
    record = [{column_name: row[index] for column_name, index in zip(select, indices)} for row in rows]
    pprint(record)


if __name__ == '__main__':
    extracting_data_from_csv_files()
