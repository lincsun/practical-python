# Sorting
#
# exercise 1.23


def sorting_test():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print('origin list: {}'.format(inst_list_0))

    inst_list_0.sort()
    print('after sort: {}'.format(inst_list_0))

    inst_list_0.sort(reverse=True)
    print('after reverse sort: {}'.format(inst_list_0))


if __name__ == '__main__':
    sorting_test()
