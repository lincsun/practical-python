# Finding out if you can retire
#
# exercise 2.7

import report


def finding_out_if_you_can_retire():
    report.cal_gain_or_loss('../../Data/portfolio.csv', '../../Data/prices.csv')


if __name__ == '__main__':
    finding_out_if_you_can_retire()
