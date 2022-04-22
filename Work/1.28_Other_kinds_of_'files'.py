# Other kinds of "files"
#
# exercise 1.28

import gzip


def other_kinds_of_files():
    with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
        for line in f:
            print(line, end='')


if __name__ == '__main__':
    other_kinds_of_files()
