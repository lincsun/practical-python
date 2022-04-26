# Picking a different column delimitier
#
# exercise 3.7
import fileparse
from pprint import pprint


def picking_a_different_column_delimitier():
    portfolio = fileparse.parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
    pprint(portfolio)


if __name__ == '__main__':
    picking_a_different_column_delimitier()
