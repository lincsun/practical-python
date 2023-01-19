# Dave's mortgage
#
# exercise 1.7

def cal_mortgage():
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    while principal > 0:
        principal = principal * (1 + rate / 12) - payment
        total_paid = total_paid + payment

    print('Total paid', round(total_paid, 1))


if __name__ == '__main__':
    cal_mortgage()
