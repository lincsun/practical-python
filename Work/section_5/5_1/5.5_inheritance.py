from stock import Stock

if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    ibm = Stock('IBM', 50, 91.23)


    class NewStock(Stock):
        def yow(self):
            print('Yow!')


    n = NewStock('ACME', 50, 123.45)
    print(n.cost())
    n.yow()

    print(NewStock.__bases__)

    print(NewStock.__mro__)

    for cls in n.__class__.__mro__:
        if 'cost' in cls.__dict__:
            print(cls)
            print(cls.__dict__['cost'])
            break
