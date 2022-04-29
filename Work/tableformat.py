# tableformat.py
#
# exercise 4.5

class TableFormatter:
    def headings(self, headers):
        """
        Emit the table headings.
        :param headers: iteration variable
        :return:
        """
        raise NotImplementedError('err!')

    def row(self, row_data):
        """
        Emit a single row of table data.
        :param row_data: iterable variable
        :return:
        """
        raise NotImplementedError('ERR!')


class TextTableFormatter(TableFormatter):
    """
    Emit a table in plain-text format.
    """

    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-' * 10 + ' ') * len(headers))

    def row(self, row_data):
        for d in row_data:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    """
    Output portfolio data in CSV format
    """

    def headings(self, headers):
        print(','.join(headers))

    def row(self, row_data):
        print(','.join(row_data))


class HTMLTableFormatter(TableFormatter):
    """
    Output portfolio data in HTML format
    """

    def headings(self, headers):
        name, shares, price, change = headers[0], headers[1], headers[2], headers[3]
        print(f'<tr><th>{name}</th><th>{shares}</th><th>{price}</th><th>{change}</th></tr>')

    def row(self, row_data):
        name, shares, price, change = row_data[0], row_data[1], row_data[2], row_data[3]
        print(f'<tr><td>{name}</td><td>{shares}</td><td>{price}</td><td>{change}</td></tr>')


class FormatError(Exception):
    pass


def create_formatter(fmt='txt') -> TableFormatter:
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        # return TableFormatter()
        raise FormatError('Unkonwn table format %s' % fmt)


def print_table(lines, attributes: list, formatter: TableFormatter):
    formatter.headings(attributes)

    for line in lines:
        select = [str(getattr(line, attr)) for attr in attributes]
        # print(select)
        formatter.row(select)
