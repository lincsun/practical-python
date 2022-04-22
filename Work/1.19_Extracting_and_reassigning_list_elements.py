<<<<<<< HEAD
# Extracting and reassigning list elements
#
# exercise 1.19


def extracting_and_reassigning():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print(inst_list_0[0], inst_list_0[1], inst_list_0[-1], inst_list_0[-2])

    inst_list_0[2] = 'AIG'
    print('after reassign idx 2 as \'AIG\': {}'.format(inst_list_0))
    print('show slice [0:3]: {}'.format(inst_list_0[0:3]))

    inst_list_0.append('BAIDU')
    print('append \'BAIDU\': {}'.format(inst_list_0))


if __name__ == '__main__':
    extracting_and_reassigning()
=======
# Extracting and reassigning list elements
#
# exercise 1.19


def extracting_and_reassigning():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print(inst_list_0[0], inst_list_0[1], inst_list_0[-1], inst_list_0[-2])

    inst_list_0[2] = 'AIG'
    print('after reassign idx 2 as \'AIG\': {}'.format(inst_list_0))
    print('show slice [0:3]: {}'.format(inst_list_0[0:3]))

    inst_list_0.append('BAIDU')
    print('append \'BAIDU\': {}'.format(inst_list_0))


if __name__ == '__main__':
    extracting_and_reassigning()
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
