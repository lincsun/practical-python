# Lists of anything
#
# exercise 1.25


def lists_of_anything():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA', 101, 102]
    print('origin list: {}'.format(inst_list_0))

    inst_list_1 = ['debug', 'nested', inst_list_0]
    print('nested list: {}'.format(inst_list_1))

    print(inst_list_1[0], inst_list_1[2], inst_list_1[2][1])


if __name__ == '__main__':
    lists_of_anything()
