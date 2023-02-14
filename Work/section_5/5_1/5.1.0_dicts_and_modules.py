# 5.1.0_dicts_and_modules.py

from stock import Stock

test_val = 1


def func1():
    print('this is func1!')


def func2():
    print('this is func2!')


class A: pass


class B: pass


class C(A, B): pass


class D(B): pass


class E(C, D): pass


if __name__ == '__main__':
    func1()
    func2()

    print(f'{globals()}')

    s = Stock('GOOG', 100, 490.1)
    print(s.__dict__)
    print(Stock.__dict__)
    print(s.__class__)

    # modifying instance means modifying the dict info
    s.shares = 177
    print(s.__dict__)

    s.date = '2023/2/14'
    print(s.__dict__)

    del s.price
    print(s.__dict__)
    print(s.__class__.__dict__)

    print(E.__bases__)
    print((E.__mro__))
