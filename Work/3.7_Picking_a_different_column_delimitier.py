# Picking a different column delimitier
#
# exercise 3.7
import fileparse


def picking_a_different_column_delimitier():
    with open('Data/portfolio.dat') as f:
        portfolio = fileparse.parse_csv(f, types=[str, int, float], delimiter=' ')

    for p in portfolio:
        print(p)


if __name__ == '__main__':
    picking_a_different_column_delimitier()
