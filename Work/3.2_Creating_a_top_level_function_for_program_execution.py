# Creating a top-level function for program execution
#
# exercise 3.2
import report


def creating_a_top_level_function_for_program_execution():
    report.portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    print()

    report.portfolio_report('Data/portfolio2.csv', 'Data/prices.csv')
    print()

    files = ['Data/portfolio.csv', 'Data/portfolio2.csv']
    for name in files:
        report.portfolio_report(name, 'Data/prices.csv')
        print()


if __name__ == '__main__':
    creating_a_top_level_function_for_program_execution()
