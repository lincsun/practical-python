# Performing Type Conversion
#
# exercise 3.5
import fileparse
from pprint import pprint


def performing_type_conversion():
    portfolio = fileparse.parse_csv('Data/portfolio.csv', types=[str, int, float])
    pprint(portfolio)


if __name__ == '__main__':
    performing_type_conversion()
