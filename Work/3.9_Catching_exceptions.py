# Catching exceptions
#
# exercise 3.9
import fileparse


def catching_exceptions():
    portfolio = fileparse.parse_csv('Data/missing.csv', types=[str, int, float])
    print(portfolio)


if __name__ == '__main__':
    catching_exceptions()
