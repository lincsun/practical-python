# Adding some headers
#
# exercise 2.11

import report


def adding_some_headers():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format(headers[0], headers[1], headers[2], headers[3]))
    print('{:->10s} {:->10s} {:->10s} {:->10s}'.format('', '', '', ''))

    report_list = report.make_report(portfolio, prices)
    for r in report_list:
        print('%10s %10d %10.2f %10.2f' % r)


if __name__ == '__main__':
    adding_some_headers()
