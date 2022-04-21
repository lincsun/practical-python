# Regular Expressions
#
# exercise 1.18

import re


def regular_expressions():
    text = 'today is 4/21/2022, tomorrow is 4/22/2022'
    print('origin string: {}'.format(text))
    print('find all dates: {}'.format(re.findall(r'\d+/\d+/\d+', text)))
    print('change order use YY/MM/DD: {}'.format(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)))


if __name__ == '__main__':
    regular_expressions()
