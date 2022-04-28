# Tabulating with Counters
#
# exercise 2.18
import report
from collections import Counter


def tabulating_with_counters():
    with open('Data/portfolio.csv') as f:
        portfolio = report.read_portfolio(f)

    holdings = Counter()
    for s in portfolio:
        holdings[s['name']] += int(s['shares'])
    print(holdings)
    print(holdings['IBM'])
    print(holdings['MSFT'])
    print(holdings.most_common(4))

    with open('Data/portfolio2.csv') as f:
        portfolio2 = report.read_portfolio(f)

    holdings2 = Counter()
    for s in portfolio2:
        holdings2[s['name']] += int(s['shares'])
    print(holdings2)

    combined = holdings + holdings2
    print(combined)


if __name__ == '__main__':
    tabulating_with_counters()
