<<<<<<< HEAD
# Debugging
#
# exercise 1.6

def bill_height_reach_tower():
    bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
    sears_height = 442  # Height (meters)
    num_bills = 1
    day = 1

    while num_bills * bill_thickness < sears_height:
        print(day, num_bills, num_bills * bill_thickness)
        day = day + 1  # raw error: undefined variable 'days', modify it as 'day'
        num_bills = num_bills * 2

    print('Number of days', day)
    print('Number of bills', num_bills)
    print('Final height', num_bills * bill_thickness)


if __name__ == '__main__':
    bill_height_reach_tower()
=======
# Debugging
#
# exercise 1.6

def bill_height_reach_tower():
    bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
    sears_height = 442  # Height (meters)
    num_bills = 1
    day = 1

    while num_bills * bill_thickness < sears_height:
        print(day, num_bills, num_bills * bill_thickness)
        day = day + 1  # raw error: undefined variable 'days', modify it as 'day'
        num_bills = num_bills * 2

    print('Number of days', day)
    print('Number of bills', num_bills)
    print('Final height', num_bills * bill_thickness)


if __name__ == '__main__':
    bill_height_reach_tower()
>>>>>>> c3b3606b64174eb1de08a843a8ae3b06bdb6414d
