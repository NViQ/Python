def remove_(integer_list, values_list):
    for i in values_list:
        try:
            while i in integer_list:
                integer_list.remove(i)
        except ValueError:
            break
    # for i in integer_list:
    #     if i in values_list:
    #         integer_list.remove(i)
    print(integer_list)

integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
values_list = [1, 3]
remove_(integer_list, values_list)#, [2, 2, 4])

integer_list = [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8]
values_list = [1, 3, 4, 2]
remove_(integer_list, values_list)#, [5, 6, 7, 8])

# class List(object):
#     def remove_(self, integer_list, values_list):
#         return [i for i in integer_list if i not in values_list]
