# Structuring a program as a collection of functions
#
# exercise 3.1
import report


def structing_a_program_as_a_collection_of_functions():
    # read a csv file and get returned list of several dicts of bought stocks' prices
    portfolio = report.read_portfolio('Data/portfolio.csv')

    # read a csv file and get returned dictionary of several stock's current prices
    prices = report.read_prices('Data/prices.csv')

    # based on portfolio and prices, get a returned list of stocks' report
    inst_list = report.make_report(portfolio, prices)

    # print report
    report.print_report(inst_list)


if __name__ == '__main__':
    structing_a_program_as_a_collection_of_functions()
