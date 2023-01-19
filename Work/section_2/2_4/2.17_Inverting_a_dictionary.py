# Inverting a dictionary
#
# exercise 2.17


def inverting_a_dictionary():
    prices = {
        'GOOG': 490.1,
        'AA': 23.45,
        'IBM': 91.1,
        'MSFT': 34.23
    }

    print(prices.items())

    price_list = list(zip(prices.values(), prices.keys()))
    print(price_list)
    print(min(price_list), max(price_list), sorted(price_list))

    a = [1, 2, 3, 4, 5, 6]
    b = ['x', 'y', 'z']
    print(list(zip(a, b)))


if __name__ == '__main__':
    inverting_a_dictionary()
