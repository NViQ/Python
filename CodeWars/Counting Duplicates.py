# def duplicate_count(ar):
#     n = 0
#     print(set(ar))
#     for i in set(ar.lower()):
#         if ar.lower().count(i) > 1:
#             n +=1
#     print(n)
#     # return len([c for c in set(s.lower()) if s.lower().count(c) > 1])
#
#
# duplicate_count(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False])


def xo(s):
    if s.lower().count('x') == s.count('o') or s.count('x') == 0 and s.count('y') == 0:
        print(True)
    else:
        print(False)



xo('xo')#, 'True expected')
xo('xo0')#, 'True expected')
xo('xxxoo')#, 'False expected')
xo('rgrgrg')
