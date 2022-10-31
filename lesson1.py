# # # https://www.tutorialspoint.com/python3/python_gui_programming.htm
# #
# import types
# from tkinter import *
#
# root = Tk()
# root.title('Мое первое GUI приложение')
# root.iconbitmap('python.ico')
# root.geometry('600x400+600+100')
# root.resizable(False, False)
# root.config(bg='#099')
# root['bg'] = 'red'
#
# root.mainloop()
#
# print(type(red))

def solution(string):
    print(string[::-1])

solution('Hello')