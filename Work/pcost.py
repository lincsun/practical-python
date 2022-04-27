# pcost.py
#
# Exercise 1.27
import sys

import report


def portfolio_cost(filename: str):
    portfolio = report.read_portfolio(filename)

    total_cost = 0
    for p in portfolio:
        total_cost += int(p.get('shares')) * float(p.get('price'))

    print('Total cost {}'.format(total_cost))


def main(argv: list):
    portfolio_cost(argv[1])


if __name__ == '__main__':
    main(sys.argv)
