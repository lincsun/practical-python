# Working without Headers
#
# exercise 3.6
import fileparse
from pprint import pprint


def working_without_headers():
    portfolio = fileparse.parse_csv('Data/prices.csv', types=[str, float], has_header=False)
    pprint(portfolio)


if __name__ == '__main__':
    working_without_headers()
