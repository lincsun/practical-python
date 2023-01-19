# report.py
#
# Exercise 2.4
import csv
from fileparse import parse_csv
# from pprint import pprint
# import sys
import stock
import tableformat


def read_portfolio(lines) -> list:
    portfolio = parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])
    return [stock.Stock(d['name'], d['shares'], d['price']) for d in portfolio]


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

    for b in bought:
        stock_name = b.name

        if stock_name in current:
            gain_loss += (b.shares * (current[stock_name] - b.price))

    print('get gain: {}'.format(gain_loss))


def print_report(report_result: list, table_formatter: tableformat):
    table_formatter.headings(['name', 'shares', 'price', 'Change'])

    for name, shares, price, change in report_result:
        table_formatter.row([str(name), str(shares), str(price), str(change)])


def make_report(portfolio: list, prices: dict) -> list:
    inst_list = []

    p: stock.Stock
    for p in portfolio:
        stock_name = p.name
        # print(stock_name)
        if stock_name not in prices:
            print('not found stock name: {}'.format(stock_name))
            continue

        # print(prices[stock_name].__class__, p.get('price').__class__)

        inst_list.append((str(p.name), int(p.shares), float(p.price),
                          round(float(prices[stock_name] - float(p.price)), 2)))
        # print('list: {}'.format(inst_list))

    return inst_list


def portfolio_report(portfolio_filename: str, price_filename: str, fmt='txt'):
    # read a csv file and get returned list of several dicts of bought stocks' prices
    with open(portfolio_filename) as f:
        portfolio: list = read_portfolio(f)

    # read a csv file and get returned dictionary of several stock's current prices
    with open(price_filename) as f:
        prices = read_prices(f)

    # based on portfolio and prices, get a returned list of stocks' report
    inst_list = make_report(portfolio, prices)
    # print(inst_list)

    # print report

    # test table formatter
    table_formatter = tableformat.create_formatter(fmt)
    print_report(inst_list, table_formatter)


def main(argv):
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    # print('get argv: {}'.format(sys.argv))
    # main(sys.argv)
