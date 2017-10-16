'''Function that deletes multiple occurances based on inpout'''


def mul(lst, times):
    new = []
    for _ in lst:
        if new.count(_) < times:
            new.append(_)
    return new
