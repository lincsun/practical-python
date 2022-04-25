# Data Extraction
#
# exercise 2.22

import report


def data_extraction():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    inst_list = [(p['name'], int(p['shares'])) for p in portfolio]
    print(inst_list)

    names = {p['name'] for p in portfolio}
    print(names)

    holdings = {name: 0 for name in names}
    print(holdings)

    for p in portfolio:
        holdings[p['name']] += int(p['shares'])
    print(holdings)

    portfolio_prices = {name: prices[name] for name in names if name in prices}
    print(portfolio_prices)


if __name__ == '__main__':
    data_extraction()
