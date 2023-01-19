# List Comprehensions
#
# exercise 2.6.0


def list_comprehensions():
    a = [1, 2, 3, 4, 5]
    b = [2 * x for x in a]
    print(b)

    a = [1, -5, 4, 2, -2, 10]
    b = [2 * x for x in a if x > 0]
    print(b)


if __name__ == '__main__':
    list_comprehensions()
