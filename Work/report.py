# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
# from pprint import pprint
import sys


def read_portfolio(lines) -> list:
    return parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])


def read_prices(lines) -> dict:
    prices_list = parse_csv(lines, types=[str, float], has_header=False)

    prices_dict = {}
    for p in prices_list:
        prices_dict[p[0]] = p[1]
    return prices_dict


def cal_gain_or_loss(bought_value_filename: str, current_value_filename: str):
    with open(bought_value_filename) as f:
        bought = read_portfolio(f)
    # pprint('get bought: {}'.format(bought))

    with open(current_value_filename) as f:
        current = read_prices(f)
    # pprint('current value: {}'.format(current))

    gain_loss = 0.0

    for i in range(len(bought)):
        stock_name = bought[i].get('name')

        if stock_name in current:
            gain_loss += (bought[i].get('shares') * (current[stock_name] - bought[i].get('price')))

    print('get gain: {}'.format(gain_loss))


def print_report(report_result: list):
    for i, r in enumerate(report_result):
        # print('1111: {}'.format(r))
        if 0 == i:
            for obj in r:
                print('{:>10s}'.format(obj), end=' ')
            print()
        elif 1 == i:
            print('{:->10s} {:->10s} {:->10s} {:->10s}'.format('', '', '', ''))
        else:
            print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'.format(r[0], int(r[1]), float(r[2]), float(r[3])))


def make_report(portfolio: list, prices: dict) -> list:
    inst_list = []

    keys = list(portfolio[0].keys())
    # print(len(portfolio))

    inst_list = []
    inst_list_labels = list(portfolio[0].keys()) + ['Change']
    inst_list.append(tuple(inst_list_labels))  # add labels

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
    with open(portfolio_filename) as f:
        portfolio = read_portfolio(f)

    # read a csv file and get returned dictionary of several stock's current prices
    with open(price_filename) as f:
        prices = read_prices(f)

    # based on portfolio and prices, get a returned list of stocks' report
    inst_list = make_report(portfolio, prices)
    # print(inst_list)

    # print report
    print_report(inst_list)


def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    # portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    print('get argv: {}'.format(sys.argv))
    main(sys.argv)
