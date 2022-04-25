# collections module
#
# exercise 2.5.0

from collections import Counter
from collections import defaultdict
from collections import deque


def collections_module():
    portfolio = [
        ('GOOG', 100, 490.1),
        ('IBM', 50, 91.1),
        ('CAT', 150, 83.44),
        ('IBM', 100, 45.23),
        ('GOOG', 75, 572.45),
        ('AA', 50, 23.15)
    ]

    # test Counter
    total_shares = Counter()
    for name, shares, price in portfolio:
        total_shares[name] += shares
    print(total_shares['IBM'])

    # test defaultdict
    holdings = defaultdict(list)
    for name, shares, price in portfolio:
        holdings[name].append((shares, price))
    print(holdings['IBM'])

    # test deque
    history = deque(maxlen=3)
    for p in portfolio:
        history.append(p)
        print(p, p.__class__)


if __name__ == '__main__':
    collections_module()
