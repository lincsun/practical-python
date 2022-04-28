# Using Inheritance to Produce Different Output
#
# exercise 4.6
from report import read_portfolio
from report import make_report
from report import read_prices
from report import print_report

import tableformat


def portfolio_report(portfolio_filename: str, price_filename: str):
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

    # CSV table formatter
    # table_formatter = tableformat.CSVTableFormatter()

    # HTML table formatter
    table_formatter = tableformat.HTMLTableFormatter()
    print_report(inst_list, table_formatter)


def using_inheritance_to_produce_different_output():
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')


if __name__ == '__main__':
    using_inheritance_to_produce_different_output()
