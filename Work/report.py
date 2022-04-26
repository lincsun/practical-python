# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename: str) -> list:
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip label row

        portfolio = [dict(zip(headers, row)) for row in rows]

    return portfolio


def read_prices(filename: str) -> dict:
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                continue

    return prices


def cal_gain_or_loss(bought_value_filename: str, current_value_filename: str):
    bought = read_portfolio(bought_value_filename)
    # pprint('get bought: {}'.format(bought))

    current = read_prices(current_value_filename)
    # pprint('current value: {}'.format(current))

    gain_loss = 0.0

    for i in range(len(bought)):
        stock_name = bought[i].get('Name')

        if stock_name in current:
            gain_loss += (bought[i].get('Shares') * (current[stock_name] - bought[i].get('Price')))

    print('get gain: {}'.format(gain_loss))


def print_report(report_result: list):
    for r in report_result:
        print(r)


def make_report(portfolio: list, prices: dict) -> list:
    inst_list = []

    keys = list(portfolio[0].keys())
    # print(len(portfolio))

    for p in portfolio:
        stock_name = p.get('name')
        # print(stock_name)
        if stock_name not in prices:
            print('not found stock name: {}'.format(stock_name))
            continue

        # print(prices[stock_name].__class__, p.get('price').__class__)
        p['Change'] = prices[stock_name] - float(p.get('price'))
        p['price'] = prices[stock_name]

        inst_list.append((p.get(keys[0]), p.get(keys[1]), p.get(keys[2]),
                          round(float(p.get('Change')), 2)))
        # print('list: {}'.format(inst_list))

    return inst_list


def portfolio_report(portfolio_filename: str, price_filename: str):
    # read a csv file and get returned list of several dicts of bought stocks' prices
    portfolio = read_portfolio(portfolio_filename)

    # read a csv file and get returned dictionary of several stock's current prices
    prices = read_prices(price_filename)

    # based on portfolio and prices, get a returned list of stocks' report
    inst_list = make_report(portfolio, prices)

    # print report
    print_report(inst_list)


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    pprint('get portfolio: {}, class: {}'.format(portfolio, portfolio.__class__))

    # cal_gain_or_loss('Data/portfolio.csv', 'Data/prices.csv')

    prices = read_prices('Data/prices.csv')
    pprint('get prices: {}, class: {}'.format(prices, prices.__class__))

    report_list = make_report(portfolio, prices)
    print_report(report_list)
