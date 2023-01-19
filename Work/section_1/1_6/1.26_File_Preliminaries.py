# File Preliminaries
#
# exercise 1.26

def read_file_whole_data():
    with open('../../Data/portfolio.csv', 'rt') as f:
        data = f.read()

    print('get data: {}'.format(data))


def read_file_by_line():
    with open('../../Data/portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

    print()


def read_line_by_line_plus_split():
    with open('../../Data/portfolio.csv', 'rt') as f:
        inst_list_0 = next(f).split(',')
        print('first line: {}'.format(inst_list_0))

        for line in f:
            inst_list_2 = line.split(',')
            print('get line: {}'.format(inst_list_2))


def file_preliminaries():
    # read while file in one time
    read_file_whole_data()

    # read from line each time
    read_file_by_line()

    # as to each line, use split process
    read_line_by_line_plus_split()


if __name__ == '__main__':
    file_preliminaries()
