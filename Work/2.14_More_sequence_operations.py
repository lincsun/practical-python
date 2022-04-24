# More sequence operations
#
# exercise 2.14


def more_sequence_operations():
    data = [4, 9, 1, 25, 16, 100, 49]
    print(min(data))
    print(max(data))
    print(sum(data))

    for n, x in enumerate(data):
        print(n, x)

    # no good
    for n in range(len(data)):
        print(data[n])


if __name__ == '__main__':
    more_sequence_operations()
