import os
import zipfile


def read_dir(folder2):
    for root, dirs, files in os.walk(folder2):
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        print(root, files, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent}{file}')


read_dir('folder2')
#
# import zipfile
# import os

# z = zipfile.ZipFile('spam.zip', 'w')        # Создание нового архива
# for root, dirs, files in os.walk('folder2'): # Список всех файлов и папок в директории folder
#     for file in files:
#         z.write(os.path.join(root,file))         # Создание относительных путей и запись файлов в архив
#
# z.close()
#
# v = zipfile.ZipFile('spam.zip', 'r')
# v.printdir()
# #
# z.close()
#
# n, m = map(int, input().split())
# matrix = [[0] * m for _ in range(n)]
# dx, dy, x, y = 0, 1, 0, 0

# for i in range(1, n * m + 1):
#     matrix[x][y] = i
#     if matrix[(x + dx) % n][(y + dy) % m]:
#         dx, dy = dy, -dx
#     x += dx
#     y += dy
# for line in matrix:
#     print(*(f'{i:<3}' for i in line), sep='')


