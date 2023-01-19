# Adding some Methods
#
# exercise 4.2
import stock


def adding_some_methods():
    s = stock.Stock('GOOG', 100, 490.10)
    print(s.cost())

    s.sell(25)
    print(s.shares)

    print(s.cost())


if __name__ == '__main__':
    adding_some_methods()
