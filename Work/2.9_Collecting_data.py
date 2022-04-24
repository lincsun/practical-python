# Collecting Data
#
# exercise 2.9

import report


def collecting_data():
    portfolio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    report_list = report.make_report(portfolio, prices)
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('Name', 'Shares', 'Price', 'Change'))
    print('{:>10s} {:>10s} {:>10s} {:>10s}'.format('', '', '', ''))

    for i in range(len(report_list)):
        print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'.format(report_list[i][0], report_list[i][1], report_list[i][2],
                                                           report_list[i][3]))


if __name__ == '__main__':
    collecting_data()
