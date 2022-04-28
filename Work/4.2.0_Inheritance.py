# Inheritance
#
# exercise 4.2.0
import stock


class MyStock(stock.Stock):
    def panic(self):
        self.sell(self.shares)

    def cost(self):
        actual_cost = super().cost()
        return 1.25 * actual_cost


def inheritance():
    s = MyStock('GOOG', 100, 490.1)
    print('before we have shares: {}'.format(s.shares))

    s.panic()
    print('after panic, we now have shares: {}'.format(s.shares))

    del s

    s = MyStock('GOOG', 100, 490.1)
    print('after redefine function \'cost\', we got cost: {}'.format(s.cost()))

    print(super(MyStock, s).cost(), s.cost())


if __name__ == '__main__':
    inheritance()
