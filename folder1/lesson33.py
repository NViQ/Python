# f = open('folder1/1.txt', 'r', encoding='utf-8')
# text = f.read(3)
# text2 = f.read()
# # print(f.encoding)
# # text = f.read()
# # f.close()
# print(text2)
# # print(text2)

lines = ['Новая строка 1', 'Новая строка 2']
f = open('1.txt', 'a', encoding='utf-8')
f.write(lines[1])
f.close()


# f = open('file.txt', 'a', encoding='utf-8')
# f.write('Новая строка\n')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('file.txt', 'a', encoding='utf-8')
# # for i in lines:
# #     f.write(i + '\n')
# # f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines)
# f.close()

# f = open('file.txt', 'r', encoding='utf-8')
# for line in f:
#     print(line, end='')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('file.txt', 'w', encoding='utf-8')
# f.writelines(f'{i}\n' for i in lines)
# f.close()




























