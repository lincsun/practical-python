# Reading CSV Files
#
# exercise 3.3
import fileparse
from pprint import pprint


def reading_csv_files():
    with open('Data/portfolio.csv') as f:
        portfolio = fileparse.parse_csv(f)

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    reading_csv_files()
