# Printing a formatted table
#
# exercise 2.10

import report


def printing_a_formatted_table():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    report_list = report.make_report(portfolio, prices)
    for r in report_list:
        print('%10s %10d %10.2f %10.2f' % r)


if __name__ == '__main__':
    printing_a_formatted_table()
