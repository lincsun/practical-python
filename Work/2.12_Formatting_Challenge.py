# Formatting Challenge
#
# exercise 2.12

import report


def formatting_challenge():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(headers[0], headers[1], headers[2], headers[3]))
    print('{:->10s} {:->10s} {:->10s} {:->10s}'.format('', '', '', ''))

    report_list = report.make_report(portfolio, prices)
    for r in report_list:
        print('{:>10s} {:>10d} {:>10s} {:>10.2f}'.format(r[0], r[1], '$' + str(r[2]), r[3]))


if __name__ == '__main__':
    formatting_challenge()
