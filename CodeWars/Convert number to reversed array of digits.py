def digitize(n):
    return [int(x) for x in str(n)[::-1]]


    # return map(int, str(n)[::-1])