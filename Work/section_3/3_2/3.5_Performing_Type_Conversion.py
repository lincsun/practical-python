# Performing Type Conversion
#
# exercise 3.5
import fileparse


def performing_type_conversion():
    with open('../../Data/portfolio.csv') as f:
        portfolio = fileparse.parse_csv(f, types=[str, int, float])

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    performing_type_conversion()
