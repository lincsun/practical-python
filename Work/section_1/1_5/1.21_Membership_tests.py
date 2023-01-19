# Membership tests
#
# exercise 1.21


def membership_test():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print(inst_list_0[0], inst_list_0[1], inst_list_0[-1], inst_list_0[-2])

    print(
        '\'AIG\' in list: {}, \'AA\' in list: {}, \'CAR\' not in list: {}'.format('AIG' in inst_list_0,
                                                                                  'AA' in inst_list_0,
                                                                                  'CAT' not in inst_list_0))


if __name__ == '__main__':
    membership_test()
