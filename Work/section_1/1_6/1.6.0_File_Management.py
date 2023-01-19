# Files Management
#
# exercise 1.6.0


def file_proc():
    a = open('../../test_fp.txt', 'wt+')
    a.write("some text\ncome on!")
    a.close()

    b = open('../../test_fp.txt', 'rt+')
    t = b.read(4)
    print('read 4 bytes from file: {}'.format(t))
    b.close()

    # automatically close file
    with open('../../test_fp.txt', 'rt') as file:
        c = file.read()
        print('c: {}'.format(c))

        file.seek(0, 0)
        for line in file:
            print('get line: {}'.format(line.strip()))


if __name__ == '__main__':
    file_proc()
