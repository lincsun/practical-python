# Using your library module
#
# exercise 3.12
import report


def using_your_library_module():
    with open('Data/portfolio.csv') as f:
        portfoliio = report.read_portfolio(f)

    with open('Data/prices.csv') as f:
        prices = report.read_prices(f)

    inst_list = report.make_report(portfoliio, prices)
    report.print_report(inst_list)


if __name__ == '__main__':
    using_your_library_module()
