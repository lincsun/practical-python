# Data Queries
#
# exercise 2.21

import report


def data_queries():
    portfolio = report.read_portfolio('Data/portfolio.csv')

    more100 = [s for s in portfolio if int(s['shares']) > 100]
    print(more100)

    msft_ibm = [s for s in portfolio if s['name'] in {'MSFT', 'IBM'}]
    print(msft_ibm)

    cost10k = [s for s in portfolio if int(s['shares']) * float(s['price']) > 10000]
    print(cost10k)


if __name__ == '__main__':
    data_queries()
