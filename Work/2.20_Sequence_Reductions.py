# Sequence Reductions
#
# exercise 2.20

import report


def sequence_reductions():
    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    cost = sum(int(p.shares) * float(p.price) for p in portfolio)
    print(cost)

    with open('Data/prices.csv') as f:
        prices = report.read_prices(f)
    value = sum(int(p.shares) * prices[p.name] for p in portfolio if p.name in prices)
    print(value)


if __name__ == '__main__':
    sequence_reductions()
