# A First Program
#
# exercise 1.2.0

def start_magic():
    print('hello world! \n')


def bill_height_reach_tower():
    bill_thickness = 0.11 * 0.001
    sears_height = 442
    num_bills = 1
    day = 1

    while num_bills * bill_thickness < sears_height:
        print('day: {}, num_bills: {}, height of bill is: {} M'.format(day, num_bills, num_bills * bill_thickness))
        num_bills *= 2
        day += 1

    print()
    print('after {} days, the height of bills over the tower! \n'.format(day))


def statement_comment_test():
    a = 3 + 4
    # this is a comment
    b = a * 2

    print(b)


def variable_test():
    height = 442  # valid
    _height = 442  # valid
    height2 = 442  # valid
    # 2height = 442  # invalid


def types_test():
    height = 442  # An integer
    height = 442.0  # Floating point
    height = 'Really tall'  # A string


def case_sensitivity_test():
    name = 'Jake'
    Name = 'Elwood'
    NAME = 'Guido'

    print(name, Name, NAME)


if __name__ == '__main__':
    # print hello world
    start_magic()

    # cal bills height reaching tower
    bill_height_reach_tower()

    # statements + comments
    statement_comment_test()

    # variables
    variable_test()

    # types
    types_test()

    # case sensitivity
    case_sensitivity_test()
