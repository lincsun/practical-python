# Reading CSV Files
#
# exercise 3.3
import fileparse
from pprint import pprint


def reading_csv_files():
    portfolio = fileparse.parse_csv('Data/portfolio.csv')
    pprint(portfolio)


if __name__ == '__main__':
    reading_csv_files()
