def nb_year(p0, percent, aug, p):
    count = 0
    while p0 <= p:
        p0 += int(p0*(percent/100)+aug)
        count += 1
    print(count)




# nb_year(1500, 5, 100, 5000)
nb_year(1500000, 2.5, 10000, 2000000)
