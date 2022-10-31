def series_sum(n):
    if n > 1:
        b = 1
        m = 4
        for i in range(1, n):
            v = round(1/m, 2)
            b += v
            m += 3
        print(format(b, '.2f'))
    else:
        print(format(n, '.2f'))

    # return '{:.2f}'.format(sum(1.0 / (3 * i + 1) for i in range(n)))







series_sum(1)
"""
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""