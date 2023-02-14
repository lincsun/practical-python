from stock import Stock

if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    ibm = Stock('IBM', 50, 91.23)

    s = goog.sell

    print(s)

    print(s(25))
    print(goog.shares)

    print(s.__func__)
    print(Stock.__dict__['sell'])

    print(s.__self__)
    
    print(s.__func__(s.__self__, 25))
    print(goog.shares)
