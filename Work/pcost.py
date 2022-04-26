# pcost.py
#
# Exercise 1.27

import report


def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)

    total_cost = 0
    for p in portfolio:
        total_cost += int(p.get('shares')) * float(p.get('price'))

    print('Total cost {}'.format(total_cost))
