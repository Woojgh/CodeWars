'''This is a function that will divide by succesive power.'''
'''1, 10, 9, 12, 3, 4'''


def suc_pow(n):
    num = 0
    suc = [1, 10, 9, 12, 3, 4]
    n = list(str(n))
    for _ in range(0, len(n)):
        num = num + (int(n[_]) * int(suc[_]))
    return num
