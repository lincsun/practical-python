# List comprehensions
#
# exercise 2.19


def list_comprehensions():
    nums = [1, 2, 3, 4]
    squares = [x ** 2 for x in nums]
    print(squares)

    twice = [x * 2 for x in nums if x > 2]
    print(twice)


if __name__ == '__main__':
    list_comprehensions()
