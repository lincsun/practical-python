# Better output for printing objects
#
# exercise 4.9
import stock
import report


def better_output_for_printing_objects():
    s = stock.Stock('GOOG', 100, 490.10)
    print(s)

    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)
        print(portfolio)


if __name__ == '__main__':
    better_output_for_printing_objects()
