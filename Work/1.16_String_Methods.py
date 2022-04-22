<<<<<<< HEAD
# String Methods
#
# exercise 1.16

def string_methods():
    s = 'AAPL,IBM,MSFT,YHOO,SCO'
    print('origin: {}'.format(s))

    s = s + ',GOOG'
    print('after append GOOG: {}'.format(s))

    s = 'HPQ,' + s
    print('add front HPQ: {}'.format(s))

    print('lower: {}'.format(s.lower()))
    print('find string \'AAPL\': {}'.format(s.find('AAPL')))
    print('show index [7:10]: {}'.format(s[7:10]))
    print('replace substring \'IBM\' to \'BAIDU\': {}'.format(s.replace('IBM', 'BAIDU')))


if __name__ == '__main__':
    string_methods()
=======
# String Methods
#
# exercise 1.16

def string_methods():
    s = 'AAPL,IBM,MSFT,YHOO,SCO'
    print('origin: {}'.format(s))

    s = s + ',GOOG'
    print('after append GOOG: {}'.format(s))

    s = 'HPQ,' + s
    print('add front HPQ: {}'.format(s))

    print('lower: {}'.format(s.lower()))
    print('find string \'AAPL\': {}'.format(s.find('AAPL')))
    print('show index [7:10]: {}'.format(s[7:10]))
    print('replace substring \'IBM\' to \'BAIDU\': {}'.format(s.replace('IBM', 'BAIDU')))


if __name__ == '__main__':
    string_methods()
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
