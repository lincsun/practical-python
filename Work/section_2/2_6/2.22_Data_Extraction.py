# Data Extraction
#
# exercise 2.22

import report


def data_extraction():
    with open('../../Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    with open('../../Data/prices.csv') as f:
        prices = report.read_prices(f)

    inst_list = [(p.name, int(p.shares)) for p in portfolio]
    print(inst_list)

    names = {p.name for p in portfolio}
    print(names)

    holdings = {name: 0 for name in names}
    print(holdings)

    for p in portfolio:
        holdings[p.name] += int(p.shares)
    print(holdings)

    portfolio_prices = {name: prices[name] for name in names if name in prices}
    print(portfolio_prices)


if __name__ == '__main__':
    data_extraction()
