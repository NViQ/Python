# def tower_builder(n):
#     print([('*'*i).center(n*2-1) for i in range(1,n*2, 2)])
#
# # tower_builder(1)#, ['*', ])
# # tower_builder(2)#, [' * ', '***'])
# tower_builder(3)#, ['  *  ', ' *** ', '*****'])

def tower_builder(n_floors, block_size):
    w, h = block_size
    l = []
    n = 1
    for i in range(w, w+w*2*(n_floors), w*2):
        while n <= h:
            l.append(('*'*i).center(w+w*2*(n_floors-1)))
            n +=1
        n = 1

    print(l)


# tower_builder(1, (1, 1))#, ['*', ])
tower_builder(3, (4, 2))#, ['        ****        ', '        ****        ', '    ************    ', '    ************    ', '********************', '********************'])