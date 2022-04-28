# Creating a list of instances
#
# exercise 4.3
import fileparse
import stock


def creating_a_list_of_instances():
    with open('Data/portfolio.csv') as f:
        portdicts = fileparse.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])

    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    print(portfolio)

    print(sum([s.cost() for s in portfolio]))


if __name__ == '__main__':
    creating_a_list_of_instances()
