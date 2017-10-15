'''Function that will reverse a string and omit non alpha characters.'''


def reverse(string):
    return ''.join([x for x in string if x.isalpha()])[::-1]
