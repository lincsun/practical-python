# An example of using getattr()
#
# exercise 4.10
import stock
import tableformat
import report


def an_example_of_using_getattr():
    s = stock.Stock('GOOG', 100, 490.10)
    print(s)

    columns = ['name', 'shares']
    for colname in columns:
        print(colname, '=', getattr(s, colname))

    with open('../../Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    formatter = tableformat.create_formatter('txt')
    tableformat.print_table(portfolio, ['name', 'shares'], formatter)

    formatter = tableformat.create_formatter('txt')
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)

    formatter = tableformat.create_formatter('csv')
    tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)


if __name__ == '__main__':
    an_example_of_using_getattr()
