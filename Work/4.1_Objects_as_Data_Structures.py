# Objects as Data Structures
#
# exercise 4.1
import stock


def objects_as_data_structures():
    inst_stock_1 = stock.Stock('AAPL', 50, 122.34)
    inst_stock_2 = stock.Stock('IBM', 75, 91.75)

    print(inst_stock_1.shares * inst_stock_1.price)
    print(inst_stock_2.shares * inst_stock_2.price)

    stocks = [inst_stock_1, inst_stock_2]
    print(stocks)

    for s in stocks:
        print(f'{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}')


if __name__ == '__main__':
    objects_as_data_structures()
