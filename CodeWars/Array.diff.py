def array_diff(a, b):
    for i in a:
        for m in b:
            try:
                if m:
                    a.remove(m)
                elif m == 0:
                    a.remove(0)
            except ValueError:
                pass
    print(a)

    # return [x for x in a if x not in b]




array_diff([10, 18, 20, -14, 8, 18, -18, -9, -14, 9, -7, 0, 12, -6, -8], [0, 13])