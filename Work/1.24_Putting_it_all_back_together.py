# Putting it all back together
#
# exercise 1.24


def putting_it_all_back_together():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print('origin list: {}'.format(inst_list_0))

    inst_list_1 = ','.join(inst_list_0)
    print('after join with \',\': {}'.format(inst_list_1))

    inst_list_2 = ':'.join(inst_list_0)
    print('after join with \':\': {}'.format(inst_list_2))

    inst_list_3 = ''.join(inst_list_0)
    print('after join with \'\': {}'.format(inst_list_3))


if __name__ == '__main__':
    putting_it_all_back_together()
