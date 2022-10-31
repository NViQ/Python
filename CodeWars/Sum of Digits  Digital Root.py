def digital_root(n):
    m = 0
    o = 0
    for i in str(n):
        m += int(i)
    if m > 9:
        for u in str(m):
            o += int(u)
        if o > 9:
            q = 0
            for i in str(o):
                q += int(i)
            if q > 9:
                w = 0
                for u in str(q):
                    w += int(u)

                if w > 9:
                    e = 0
                    for i in str(w):
                        e += int(i)
                    print(e)
                else:
                    print(w)
            else:
                print(q)
        else:
            print(o)
    else:
        print(m)
#
# def digital_root(n):
#     print(n if n < 10 else digital_root(sum(map(int,str(n)))))
#     #
    # while n > 9:
    #     n = sum(map(int, str(n)))
    # return n


digital_root(493197777774555555555555555555555555555555555555555555555555555555555555555555555555555555555544444444444444444444447777777773)