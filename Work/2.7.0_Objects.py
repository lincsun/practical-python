# Objects
#
# exercise 2.7.0
import copy


def objects_test():
    a = [1, 2, [10, 11], 3]
    b = a
    c = [a, b]
    print(a, b, c)

    a.append(999)  # effect four different references
    print(a, b, c)

    d = list(a)
    print(a is d, a == d, id(a), id(d))

    a[2].append(12)
    print(a[2], d[2], a[2] is d[2])  # shallow copy

    b = copy.deepcopy(a)
    a[2].append(13)
    print(a[2], b[2], a[2] is b[2])  # deep copy

    print(type(a), isinstance(a, list))


if __name__ == '__main__':
    objects_test()
