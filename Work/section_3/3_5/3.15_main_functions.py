# main() functions
#
# exercise 3.15
import report
import pcost


def main_functions():
    argv = ['report.py', '../../Data/portfolio.csv', '../../Data/prices.csv']
    report.main(argv)

    argv = ['pcost.py', '../../Data/portfolio.csv']
    pcost.main(argv)


if __name__ == '__main__':
    main_functions()
