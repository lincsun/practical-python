# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)  # skip label row

        for row in rows:
            portfolio.append(dict(zip(headers, row)))

    return portfolio


def read_prices(filename):
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except:
                continue

    return prices


def cal_gain_or_loss(bought_value_filename, current_value_filename):
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


def make_report(portfolio, prices):
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
                          p.get('Change')))
        # print('list: {}'.format(inst_list))

    return inst_list


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    pprint('get portfolio: {}, class: {}'.format(portfolio, portfolio.__class__))

    # cal_gain_or_loss('Data/portfolio.csv', 'Data/prices.csv')

    prices = read_prices('Data/prices.csv')
    pprint('get prices: {}, class: {}'.format(prices, prices.__class__))

    report_list = make_report(portfolio, prices)
    for r in report_list:
        print('get report list: {}'.format(r))
