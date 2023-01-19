# pcost.py
#
# Exercise 1.27
import sys

import report
import stock


def portfolio_cost(filename: str):
    with open(filename) as f:
        portfolio = report.read_portfolio(f)

    total_cost = 0
    p: stock.Stock
    for p in portfolio:
        total_cost += int(p.shares) * float(p.price)
    print('Total cost {}'.format(total_cost))


def main(argv: list):
    portfolio_cost(argv[1])


if __name__ == '__main__':
    # func when used in cmdline
    # main(sys.argv)

    main(['report.py', 'Data/portfolio.csv'])
