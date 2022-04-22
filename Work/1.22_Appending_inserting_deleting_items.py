<<<<<<< HEAD
# Appending, inserting, and deleting items
#
# exercise 1.22


def append_insert_delete_item():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print('origin list: {}'.format(inst_list_0))

    inst_list_0.append('BAIDU')
    print('after append: {}'.format(inst_list_0))

    inst_list_0.insert(1, 'ALIBABA')
    print('after insert: {}'.format(inst_list_0))

    inst_list_0.remove('GOOG')
    print('after remove: {}'.format(inst_list_0))

    del inst_list_0[1]
    print('after delete index 1 item: {}'.format(inst_list_0))
    print('show index 1 item: {}'.format(inst_list_0[1]))
    print('show the count of item \'BAIDU\' exist: {}'.format(inst_list_0.count('BAIDU')))

    inst_list_0.insert(1, 'BAIDU')
    print('insert \'BAIDU\' at index 1: {}'.format(inst_list_0))

    inst_list_0.remove('BAIDU')
    print('remove the first occurance item of \'BAIDU\': {}'.format(inst_list_0))


if __name__ == '__main__':
    append_insert_delete_item()
=======
# Appending, inserting, and deleting items
#
# exercise 1.22


def append_insert_delete_item():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print('origin list: {}'.format(inst_list_0))

    inst_list_0.append('BAIDU')
    print('after append: {}'.format(inst_list_0))

    inst_list_0.insert(1, 'ALIBABA')
    print('after insert: {}'.format(inst_list_0))

    inst_list_0.remove('GOOG')
    print('after remove: {}'.format(inst_list_0))

    del inst_list_0[1]
    print('after delete index 1 item: {}'.format(inst_list_0))
    print('show index 1 item: {}'.format(inst_list_0[1]))
    print('show the count of item \'BAIDU\' exist: {}'.format(inst_list_0.count('BAIDU')))

    inst_list_0.insert(1, 'BAIDU')
    print('insert \'BAIDU\' at index 1: {}'.format(inst_list_0))

    inst_list_0.remove('BAIDU')
    print('remove the first occurance item of \'BAIDU\': {}'.format(inst_list_0))


if __name__ == '__main__':
    append_insert_delete_item()
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
