# Polymorphism in Action
#
# exercise 4.7
import report


def polymorphism_in_action():
    report.portfolio_report('../../Data/portfolio.csv', '../../Data/prices.csv', fmt='txt')
    report.portfolio_report('../../Data/portfolio.csv', '../../Data/prices.csv', fmt='csv')
    report.portfolio_report('../../Data/portfolio.csv', '../../Data/prices.csv', fmt='html')


if __name__ == '__main__':
    polymorphism_in_action()
