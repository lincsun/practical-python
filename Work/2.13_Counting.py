# Counting
#
# exercise 2.13


def counting():
    for n in range(10):
        print(n, end=' ')

    for n in range(10, 0, -1):
        print(n, end=' ')

    for n in range(0, 10, 2):
        print(n, end=' ')


if __name__ == '__main__':
    counting()
