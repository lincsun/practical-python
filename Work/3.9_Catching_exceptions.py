# Catching exceptions
#
# exercise 3.9
import fileparse


def catching_exceptions():
    with open('Data/missing.csv') as f:
        portfolio = fileparse.parse_csv(f, types=[str, int, float])

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    catching_exceptions()
