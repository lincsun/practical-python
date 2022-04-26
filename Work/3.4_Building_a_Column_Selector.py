# Building a Column Selector
#
# exercise 3.4
import fileparse
from pprint import pprint


def reading_csv_files():
    portfolio = fileparse.parse_csv('Data/portfoliodate.csv', select=None)
    pprint(portfolio)


if __name__ == '__main__':
    reading_csv_files()
