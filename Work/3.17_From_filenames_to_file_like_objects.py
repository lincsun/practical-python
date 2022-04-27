# From filenames to file-like objects
#
# exercise 3.17
import report
import pcost


def making_scripts():
    argv = ['report.py', 'Data/portfolio.csv', 'Data/prices.csv']
    report.main(argv)

    argv = ['pcost.py', 'Data/portfolio.csv']
    pcost.main(argv)


if __name__ == '__main__':
    making_scripts()
