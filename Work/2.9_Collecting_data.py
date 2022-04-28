# Collecting Data
#
# exercise 2.9

import report


def collecting_data():
    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    with open('Data/prices.csv') as f:
        prices = report.read_prices(f)

    report_list = report.make_report(portfolio, prices)
    report.print_report(report_list)


if __name__ == '__main__':
    collecting_data()
