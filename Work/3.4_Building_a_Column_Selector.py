# Building a Column Selector
#
# exercise 3.4
import fileparse


def reading_csv_files():
    with open('Data/portfolio.csv') as f:
        portfolio = fileparse.parse_csv(f, select=None)

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    reading_csv_files()
