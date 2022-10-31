def find_nb(m):
    n = (-1 + (1 + 8 * (m ** (0.5))) ** 0.5) / 2
    if int(n) == float(n):
        print(n)
    else:
        print(-1)


find_nb(135440716410000)# 2022
find_nb(859121438695041601)# -1