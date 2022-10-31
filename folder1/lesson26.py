# def hello(name, word):
#     print('Hello, ' + name + '. Say ' + word)
#
# hello('John', 'hi')
# hello('Katy', 'hello')


# def get_sum(a, b):
#     print(a + b)


# x = 2
# y = 5
# get_sum(1, 3)
# get_sum(x, y)

# print(len('Hello'))

# def get_sum(a, b):
#     return a + b
#
# print(get_sum(1, 2))

# def hi():
#     print('Hi')
#
# hi()

# def tabl(a=2, b=9, c=2, d=9):
#     '''
#     Выводит таблицу умножения.
#
#     :param a: С какого операнда выводить таблицу
#     :type a: int
#     :param b: До какого операнда выводить таблицу
#     :type b: int
#     :param c: С какого операнда начинать перемножать
#     :type c: int
#     :param d: До какого операнда начинать перемножать
#     :type d: int
#     '''
#     for i in range (c, (d+1)):
#         for k in range (a, (b+1)):
#             print(f'{k} * {i} = {i * k}\t', end='')
#         print('')
#
# tabl(1,2,d=5)
#
# def time_l (time):
#     return int(time//2)
# # time1 = 3 # litres = 1
# # time2 = 6.7 # litres = 3
# # time3 = 11.8 # litres = 5
#
# time_l(3)
# y = (time_l(3))*2 + time_l(6.7) + time_l(11.8)
# print(f'\n{y}')
#
# print(int(time1 // 2))
# print(int(time2 // 2))
# print(int(time3 // 2))

l = [1,2,3]

def f ():
    l2 = [i * 2 for i in l]
    print(l2)
f()




