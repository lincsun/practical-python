# Dave's mortgage with extras
#
# exercise 1.8

def cal_mortgage_with_extras():
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    month_cnt = 0

    while principal > 0:
        month_cnt += 1

        if month_cnt <= 12:
            real_payment = payment + 1000
        else:
            real_payment = payment

        principal = principal * (1 + rate / 12) - real_payment
        total_paid = total_paid + real_payment

    print('Total paid: {}, used month: {}'.format(round(total_paid, 2), month_cnt))


if __name__ == '__main__':
    cal_mortgage_with_extras()
