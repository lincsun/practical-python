# Dave's mortgage Bonus
#
# exercise 1.11

def cal_mortgage_showing_table():
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    month_cnt = 0
    extra_payment_start_month = 61
    extra_payment_end_month = 108
    extra_payment = 1000

    while principal > 0:
        month_cnt += 1

        if extra_payment_start_month <= month_cnt <= extra_payment_end_month:
            real_payment = payment + extra_payment
        else:
            real_payment = payment

        while principal * (1 + rate / 12) < real_payment:
            real_payment = principal * (1 + rate / 12)

        principal = principal * (1 + rate / 12) - real_payment
        total_paid = total_paid + real_payment

        print(month_cnt, round(total_paid, 2), round(principal, 2))

    print()
    print('Total paid: {}, used month: {}'.format(round(total_paid, 2), month_cnt))


if __name__ == '__main__':
    cal_mortgage_showing_table()
