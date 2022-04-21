# String concatenation
#
# exercise 1.14

def string_concatenation():
    s = 'AAPL,IBM,MSFT,YHOO,SCO'
    print('origin: {}'.format(s))

    s = s + ',GOOG'
    print('after append GOOG: {}'.format(s))

    s = 'HPQ,' + s
    print('add front HPQ: {}'.format(s))


if __name__ == '__main__':
    string_concatenation()
