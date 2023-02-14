from stock import Stock

if __name__ == '__main__':
    goog = Stock('GOOG', 100, 490.10)
    ibm = Stock('IBM', 50, 91.23)

    print(goog.__class__)
    print(ibm.__class__)

    print(goog.cost())
    print(ibm.cost())

    print(Stock.__dict__['cost'])

    print(Stock.__dict__['cost'](goog))
    print(Stock.__dict__['cost'](ibm))

    Stock.foo = 42

    print(goog.foo)
    print(ibm.foo)

    print(goog.__dict__)


    class Foo(object):
        a = 13

        def __init__(self, b):
            self.b = b


    f = Foo(10)
    g = Foo(20)

    print(f.a)
    print(g.a)
    print(f.b)
    print(g.b)

    Foo.a = 42

    print(f.a)
    print(g.a)
