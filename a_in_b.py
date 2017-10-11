'''Function that will return a list of items form a that are not in b.'''


def not_in_b(a,b):
    new_list = []
    for i in a:
        if i not in b:
            new_list.append(i)
    return new_list


def shorter_not_in_b(a,b):
    return [x for x in a if x not in b]
