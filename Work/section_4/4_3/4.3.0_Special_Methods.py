# Special Methods
#
# exercise 4.3.0
import stock


def special_methods():
    s = stock.Stock('GOOG', 100, 490.10)

    print(getattr(s, 'name'))
    print(getattr(s, 'shares'))
    setattr(s, 'shares', 120)
    print(getattr(s, 'shares'))


if __name__ == '__main__':
    special_methods()
