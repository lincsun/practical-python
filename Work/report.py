# report.py
#
# Exercise 2.4
import csv
from pprint import pprint


def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)  # skip label row

        for row in rows:
            portfolio.append({'Name': row[0], 'Shares': int(row[1]), 'Price': float(row[2])})

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

    for i in range(len(portfolio)):
        stock_name = portfolio[i].get('Name')
        # print(stock_name)
        if stock_name not in prices:
            print('not found stock name: {}'.format(stock_name))
            continue

        portfolio[i]['Change'] = prices[stock_name] - portfolio[i].get('Price')
        portfolio[i]['Price'] = prices[stock_name]

        inst_list.append((portfolio[i].get(keys[0]), portfolio[i].get(keys[1]), portfolio[i].get(keys[2]),
                          portfolio[i].get('Change')))
        # print('list: {}'.format(inst_list))

    return inst_list


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    pprint('get portfolio: {}, class: {}'.format(portfolio, portfolio.__class__))

    # cal_gain_or_loss('Data/portfolio.csv', 'Data/prices.csv')

    prices = read_prices('Data/prices.csv')
    pprint('get prices: {}, class: {}'.format(prices, prices.__class__))

    report_list = make_report(portfolio, prices)
    for i in range(len(report_list)):
        print('get report list: {}'.format(report_list[i]))
