# Silencing Errors
#
# exercise 3.10
import fileparse


def silencing_errors():
    with open('Data/missing.csv') as f:
        portfolio = fileparse.parse_csv(f, types=[str, int, float], silence_errors=True)

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    silencing_errors()
