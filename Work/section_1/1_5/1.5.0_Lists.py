# Lists
#
# exercise 1.5.0


def pr_list():
    a = 'hello world'
    inst_l = a.split(' ')
    print('get list: {}'.format(inst_l))

    inst_l.append('test')
    print('after append string \'test\': {}'.format(inst_l))

    inst_l.sort()
    print('after sort: {}'.format(inst_l))

    inst_2 = inst_l * 3
    print('after multiple 3: {}'.format(inst_2))


if __name__ == '__main__':
    pr_list()
