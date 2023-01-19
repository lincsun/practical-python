# Putting it all together
#
# exercise 4.8
import sys

import report


def putting_it_all_together():
    report.portfolio_report('../../Data/portfolio.csv', '../../Data/prices.csv', fmt='txt')
    report.portfolio_report('../../Data/portfolio.csv', '../../Data/prices.csv', fmt='csv')
    report.portfolio_report('../../Data/portfolio.csv', '../../Data/prices.csv', fmt='html')


def main(argv):
    print(argv)
    report.portfolio_report(argv[1], argv[2], argv[3])


if __name__ == '__main__':
    putting_it_all_together()

    # run py script through cmdline
    # main(sys.argv)
