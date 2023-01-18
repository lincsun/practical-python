# Printing a formatted table
#
# exercise 2.10

import report
import tableformat


def printing_a_formatted_table():
    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    with open('Data/prices.csv') as f:
        prices = report.read_prices(f)

    report_list = report.make_report(portfolio, prices)
    table_formatter = tableformat.create_formatter('txt')
    report.print_report(report_list, table_formatter)


if __name__ == '__main__':
    printing_a_formatted_table()
