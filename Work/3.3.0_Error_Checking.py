# Error Checking
#
# exercise 3.3.0


def error_checking(a, b):
    try:
        a + b
    except Exception as e:
        print('err, reason:', e)
    finally:
        print('end anyway.')


if __name__ == '__main__':
    error_checking(1, 2)
    error_checking(1, '2')
