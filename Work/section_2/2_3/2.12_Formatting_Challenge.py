# Formatting Challenge
#
# exercise 2.12

import report
import tableformat


def formatting_challenge():
    with open('../../Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    with open('../../Data/prices.csv') as f:
        prices = report.read_prices(f)

    report_list = report.make_report(portfolio, prices)
    table_formatter = tableformat.create_formatter('txt')
    report.print_report(report_list, table_formatter)


if __name__ == '__main__':
    formatting_challenge()
