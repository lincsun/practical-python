# Working without Headers
#
# exercise 3.6
import fileparse


def working_without_headers():
    with open('Data/portfolio.csv') as f:
        portfolio = fileparse.parse_csv(f, types=[str, float], has_header=False)

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    working_without_headers()
