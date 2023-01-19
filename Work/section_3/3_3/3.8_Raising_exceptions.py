# Raising exceptions
#
# exercise 3.8
import fileparse


def raising_exceptions():
    with open('../../Data/portfolio.dat') as f:
        fileparse.parse_csv(f, select=['name', 'shares'], has_header=False)


if __name__ == '__main__':
    raising_exceptions()
