def get_sum(a, b):
    if a > b:
        start = a
        end = b
        result = 0
        while start != end:
            result += start
            start -= 1
        result += end
        return result
    else:
        start = b
        end = a
        result = 0
        while start != end:
            result += start
            start -= 1
        result += end
        return result
