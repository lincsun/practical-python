# Using your library module
#
# exercise 3.12
import report


def using_your_library_module():
    portfoliio = report.read_portfolio('Data/portfolio.csv')
    prices = report.read_prices('Data/prices.csv')

    inst_list = report.make_report(portfoliio, prices)
    report.print_report(inst_list)


if __name__ == '__main__':
    using_your_library_module()
