<<<<<<< HEAD
# Membership testing (substring testing)
#
# exercise 1.15

def membership_testing():
    s = 'AAPL,IBM,MSFT,YHOO,SCO'
    print('origin: {}'.format(s))

    s = s + ',GOOG'
    print('after append GOOG: {}'.format(s))

    s = 'HPQ,' + s
    print('add front HPQ: {}'.format(s))

    # 'AA' found in string s, because it's string 'AAPL' has the substring 'AA'
    print('IBM' in s, 'AA' in s, 'CAT' in s)


if __name__ == '__main__':
    membership_testing()
=======
# Membership testing (substring testing)
#
# exercise 1.15

def membership_testing():
    s = 'AAPL,IBM,MSFT,YHOO,SCO'
    print('origin: {}'.format(s))

    s = s + ',GOOG'
    print('after append GOOG: {}'.format(s))

    s = 'HPQ,' + s
    print('add front HPQ: {}'.format(s))

    # 'AA' found in string s, because it's string 'AAPL' has the substring 'AA'
    print('IBM' in s, 'AA' in s, 'CAT' in s)


if __name__ == '__main__':
    membership_testing()
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
