# Silencing Errors
#
# exercise 3.10
import fileparse


def silencing_errors():
    portfolio = fileparse.parse_csv('Data/missing.csv', types=[str, int, float], silence_errors=True)
    print(portfolio)


if __name__ == '__main__':
    silencing_errors()
