# Strings
#
# exercise 1.4.0


def pr_string():
    a = '''test!
    11111
    change line!
    '''
    print(a, a[5])

    b = ' test'
    print('show the 3rd character of this string! {}'.format(b[2]))

    c = 'DEBUG'
    d = b + c + '! '
    print('origin: {}, after strip: {}, after lower: {}, after upper: {}, after replace: {}'.format(d, d.strip(),
                                                                                                    d.lower(),
                                                                                                    d.upper(),
                                                                                                    d.replace('DEBUG',
                                                                                                              'BUG')))

    e = 123
    print('convert num 2 string: {}, {}'.format(str(e), str(e).__class__))


if __name__ == '__main__':
    pr_string()
