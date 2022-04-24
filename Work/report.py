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
            portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})

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
        stock_name = bought[i].get('name')

        if stock_name in current:
            gain_loss += (bought[i].get('shares') * (bought[i].get('price') - current[stock_name]))

    print('get gain: {}'.format(gain_loss))


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')
    print('get: {}, class: {}'.format(portfolio, portfolio.__class__))

    cal_gain_or_loss('Data/portfolio.csv', 'Data/prices.csv')
