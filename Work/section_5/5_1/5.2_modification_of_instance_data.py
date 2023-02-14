from stock import Stock

if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    ibm = Stock('IBM', 50, 91.23)

    goog.date = '6/11/2007'
    print(goog.__dict__)
    print(Stock.__dict__)

    print(ibm.__dict__)

    goog.__dict__['time'] = '9:45am'
    print(goog.time)
