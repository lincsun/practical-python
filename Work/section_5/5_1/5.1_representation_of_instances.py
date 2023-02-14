from stock import Stock

if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    ibm = Stock('IBM', 50, 91.23)

    print(goog.__dict__)
    print(ibm.__dict__)
