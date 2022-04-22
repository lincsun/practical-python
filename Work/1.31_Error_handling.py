# Error handling
#
# exercise 1.31

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        inst_list_0 = next(f).split(',')
        print('first line: {}'.format(inst_list_0))

        total = 0

        for line in f:
            inst_list_2 = line.split(',')
            try:
                total += (int(inst_list_2[1]) * float(inst_list_2[2]))
            except ValueError:
                print('invalid value!')
                # raise ValueError('invalid!')

        print('Total cost: {}'.format(total))


def error_handling():
    portfolio_cost('Data/missing.csv')


if __name__ == '__main__':
    error_handling()
