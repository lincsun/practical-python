# Looping over list items
#
# exercise 1.20


def loop_over_list_items():
    inst_list_0 = ['HPQ', 'AAPL', 'GOOG', 'DOA']
    print(inst_list_0[0], inst_list_0[1], inst_list_0[-1], inst_list_0[-2])

    for item in inst_list_0:
        print(item)


if __name__ == '__main__':
    loop_over_list_items()
