# Printing a formatted table
#
# exercise 2.10

import report


def printing_a_formatted_table():
    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    with open('Data/prices.csv') as f:
        prices = report.read_prices(f)

    report_list = report.make_report(portfolio, prices)
    report.print_report(report_list)


if __name__ == '__main__':
    printing_a_formatted_table()
