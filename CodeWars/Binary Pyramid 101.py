<<<<<<< HEAD
def binary_pyramid(m,n):
    l = []
    for i in range(m, n+1):
        l.append(int(bin(i)[2:]))
    print(bin(sum(l)))

    # return bin(sum(int(bin(i)[2:]) for i in range(m, n + 1)))[2:]
=======
# def binary_pyramid(m,n):
#     l = []
#     for i in range(m, n+1):
#         l.append(int(bin(i)[2:]))
#     print(bin(sum(l)))
#
#     # return bin(sum(int(bin(i)[2:]) for i in range(m, n + 1)))[2:]
#
#
#
#
# binary_pyramid(1,4)#,"1111010")
# binary_pyramid(1,6)#, "101001101")
# binary_pyramid(6,20)#, "1110010110100011")
# binary_pyramid(21,60)#, "1100000100010001010100")

def vlan(n):
    b = n.split()
    for i in range(1001,1301):
        b[2] = i
        print(' '.join(map(str, b)))
>>>>>>> origin/master




<<<<<<< HEAD
binary_pyramid(1,4)#,"1111010")
binary_pyramid(1,6)#, "101001101")
binary_pyramid(6,20)#, "1110010110100011")
binary_pyramid(21,60)#, "1100000100010001010100")
=======
vlan('config vlan 1001 delete 25')
>>>>>>> origin/master
