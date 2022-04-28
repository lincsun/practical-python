# stock.py
#
# exercise 4.1

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, sell):
        self.shares -= sell


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    print('name:{}, shares:{}, price:{}'.format(s.name, s.shares, s.price))
