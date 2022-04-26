# Raising exceptions
#
# exercise 3.8
import fileparse


def raising_exceptions():
    fileparse.parse_csv('Data/prices.csv', select=['name', 'shares'], has_header=False)


if __name__ == '__main__':
    raising_exceptions()
