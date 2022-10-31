from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title('УмножноСложитель')
# root.iconbitmap('16.ico')
root.geometry('320x330+600+100')
root.resizable(False, False)
root.config(bg='grey')


btn_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '+',
    'C','0', '=', '-'
]

Theme = {
    "light": {
        "but_bg": "#D3D3D3", "but_fg": "#000", "act_bg": "#7CFC00", "e_bg": "#fff"
    },
    "dark": {
        "but_bg": "#191970", "but_fg": "#fff", "act_bg": "#7CFC00", "e_bg": "#fff"
    }

    }
big_list = []
l_text = []
konech=[]

e1 = Entry(root, font=("Comic Sans MS", 20), bg=Theme['light']['e_bg'])
e1.grid(row=1, columnspan=4, sticky=W + E)
e2 = Entry(root, font=("Comic Sans MS", 20), bg=Theme['light']['e_bg'])
e2.grid(row=1, columnspan=4, sticky=W + E)
e3 = Entry(root, font=("Comic Sans MS", 10), bg='grey')
e3.grid(row=0, columnspan=4, sticky=W + E)

class Kalk:
    row = 1
    column = 0
    l_text = []

    def __init__(self, root, e1, e2, list):
        # self.big = big
        self.root = root
        self.e1 = e1
        self.e2 = e2
        self.list = list
        self.m = 0


    def cr_butt(self):

        global Theme
        Theme = {
            "light": {
                "but_bg": "#D3D3D3", "but_fg": "#000", "act_bg": "#7CFC00", "e_bg": "#fff"
            },
            "dark": {
                "but_bg": "#1A191C", "but_fg": "#87848D", "act_bg": "#453D57", "e_bg": "#726F77"
            } }

        row = 2
        column = 0

        for i in self.list:
            bnt = Button(self.root, text=i, bg=Theme['light']['but_bg'], fg=Theme['light']['but_fg'], activebackground=Theme['light']['act_bg'], width=4, font=("Comic Sans MS", 20),height=1)
            bnt.grid(row=row, column=column, sticky=W+E)
            l_text.append(bnt['text'])
            big_list.append(bnt)
            column += 1
            if column == 4:
                column = 0
                row += 1


    def butt1(self):
        global l_text, konech
        l_data = []
        l_data.append(1)
        l_data.append(2)
        # print(l_data)

        def clicked1(argu):
            if l_data[1] == '*':
                l_data.append(e1.get())
                c1 = float(l_data[0])
                c2 = float(l_data[2])
                self.e1.delete(0, END)
                self.e1.insert(END, f'{c1*c2}')
                self.e2.delete(0, END)
                self.e2.insert(END, f'{c1 * c2}')
                l_data.clear()
                l_data.append(e1.get())
                self.e1.delete(0, END)
                self.e1.insert(END, argu)
                self.e2.insert(END, argu)
                l_data.append(e1.get())
                self.e1.delete(0, END)
                # print(l_data)
            elif l_data[1] == '+':
                l_data.append(e1.get())
                c1 = float(l_data[0])
                c2 = int(l_data[2])
                self.e1.delete(0, END)
                self.e1.insert(END, f'{c1+c2}')
                self.e2.delete(0, END)
                self.e2.insert(END, f'{c1 + c2}')
                l_data.clear()
                l_data.append(e1.get())
                self.e1.delete(0, END)
                self.e1.insert(END, argu)
                self.e2.insert(END, argu)
                l_data.append(e1.get())
                self.e1.delete(0, END)
                # print(l_data)
            elif l_data[1] == '-':
                l_data.append(e1.get())
                c1 = float(l_data[0])
                c2 = int(l_data[2])
                self.e1.delete(0, END)
                self.e1.insert(END, f'{c1-c2}')
                self.e2.delete(0, END)
                self.e2.insert(END, f'{c1 - c2}')
                l_data.clear()
                l_data.append(e1.get())
                self.e1.delete(0, END)
                self.e1.insert(END, argu)
                self.e2.insert(END, argu)
                l_data.append(e1.get())
                self.e1.delete(0, END)
                # print(l_data)
            elif l_data[1] == '/':
                l_data.append(e1.get())
                c1 = float(l_data[0])
                c2 = int(l_data[2])
                self.e1.delete(0, END)
                c3 = c1 / c2
                self.e1.insert(END, f'{round(c3, 2)}')
                self.e2.delete(0, END)
                self.e2.insert(END, f'{round(c3, 2)}')
                l_data.clear()
                l_data.append(e1.get())
                self.e1.delete(0, END)
                self.e1.insert(END, argu)
                self.e2.insert(END, argu)
                l_data.append(e1.get())
                self.e1.delete(0, END)
                # print(l_data)
            else:
                l_data.clear()
                l_data.append(e1.get())
                self.e1.delete(0, END)
                self.e1.insert(END, argu)
                self.e2.insert(END, argu)
                l_data.append(argu)
                self.e1.delete(0, END)
                # print(l_data)

        def clicked5():
            self.e1.delete(0,END)
            self.e2.delete(0, END)
            l_data.clear()
            l_data.append(1)
            l_data.append(2)
            # print(l_data)

        def clicked():
            l_data.append(e1.get())
            c1 = float(l_data[0])
            c2 = int(l_data[2])
            # print(l_data)
            e3.delete(0, END)


            if l_data[1] == '/':
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                c3 = c1 / c2
                self.e1.insert(END, f' {c1} / {c2} = {round(c3,2)}')
                self.e2.insert(END, f' {c1} / {c2} = {round(c3, 2)}')
                konech.append(e2.get())
                e3.insert(END, konech[-1])
                # print(l_data)

            elif l_data[1] == '*':
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e1.insert(END, f' {c1} * {c2} = {c1*c2}')
                self.e2.insert(END, f' {c1} * {c2} = {c1 * c2}')
                konech.append(e2.get())
                e3.insert(END, konech[-1])
                # print(l_data)

            elif l_data[1] == '+':
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e1.insert(END, f' {c1} + {c2} = {c1+c2}')
                self.e2.insert(END, f' {c1} + {c2} = {c1 + c2}')
                konech.append(e2.get())
                e3.insert(END, konech[-1])
                # print(l_data)

            elif l_data[1] == '-':
                self.e1.delete(0, END)
                self.e2.delete(0, END)
                self.e1.insert(END, f' {c1} - {c2} = {c1-c2}')
                self.e2.insert(END, f' {c1} - {c2} = {c1 - c2}')
                konech.append(e2.get())
                e3.insert(END, konech[-1])
                # print(l_data)

            l_data.clear()
            l_data.append(1)
            l_data.append(2)
            # print(l_data)


        def lamb(arg):
            self.e1.insert(END, arg)
            self.e2.insert(END, arg)


        for n in big_list:

            if n['text'] == l_text[0]:
                n.config(command=lambda: lamb(l_text[0]))

            elif n['text'] == l_text[1]:
                n.config(command=lambda: lamb(l_text[1]))

            elif n['text'] == l_text[2]:
                n.config(command=lambda: lamb(l_text[2]))

            elif n['text'] == l_text[4]:
                n.config(command=lambda: lamb(l_text[4]))

            elif n['text'] == l_text[5]:
                n.config(command=lambda: lamb(l_text[5]))

            elif n['text'] == l_text[6]:
                n.config(command=lambda: lamb(l_text[6]))

            elif n['text'] == l_text[8]:
                n.config(command=lambda: lamb(l_text[8]))

            elif n['text'] == l_text[9]:
                n.config(command=lambda: lamb(l_text[9]))

            elif n['text'] == l_text[10]:
                n.config(command=lambda: lamb(l_text[10]))

            elif n['text'] == l_text[13]:
                n.config(command=lambda: lamb(l_text[13]))

            elif n['text'] == l_text[3]:
                n.config(command=lambda: clicked1(l_text[3]))

            elif n['text'] == l_text[7]:
                n.config(command=lambda: clicked1(l_text[7]))

            elif n['text'] == l_text[11]:
                n.config(command=lambda: clicked1(l_text[11]))

            elif n['text'] == l_text[15]:
                n.config(command=lambda: clicked1(l_text[15]))

            elif n['text'] == l_text[12]:
                n.config(command=clicked5)

            elif n['text'] == l_text[14]:
                n.config(command=clicked)

    def run(self):
        self.cr_butt()
        self.butt1()

butt = Kalk(root, e1, e2, btn_list)
butt.run()

def change_theme_1(theme):
    global big_list, l_text, btn_list, root, butt, main_menu
    big_list.clear()
    row = 2
    column = 0
    for i in btn_list:
        bnt = Button(root, text=i, bg=Theme['dark']['but_bg'], fg=Theme['dark']['but_fg'],
                     activebackground=Theme['dark']['act_bg'], width=4, font=("Comic Sans MS", 20), height=1)
        bnt.grid(row=row, column=column, sticky=W + E)
        l_text.append(bnt['text'])
        big_list.append(bnt)
        column += 1
        if column == 4:
            column = 0
            row += 1
    e1['bg'] = Theme['dark']['e_bg']
    e2['bg'] = Theme['dark']['e_bg']
    e3['bg'] = '#1A191C'
    e3['fg'] = 'grey'
    root.config(bg='#191970')
    main_menu['bg'] = '#191970'
    butt.butt1()

def about_program():
    messagebox.showinfo(title='Об УмножноСложителе...', message='Программа из серии: "Кумкуляторы", Версия 3.6')

def kalk_quit():
    answer = messagebox.askokcancel(title="Выход", message='Закрыть программу?')
    if answer:
        root.destroy()
def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(("Текстовые документы (*.txt)", "*.txt"), ("Все файлы", "*.*")))
    f = open(file_path, 'w', encoding='utf-8')
    n = str(konech)
    f.write(n)
    f.close()

def print_history():
    messagebox.showinfo(title='История операций:', message=konech)


def change_theme_2(theme):
    global big_list, l_text, btn_list, root, butt
    big_list.clear()
    row = 2
    column = 0
    for i in btn_list:
        bnt = Button(root, text=i, bg=Theme['light']['but_bg'], fg=Theme['light']['but_fg'],
                     activebackground=Theme['light']['act_bg'], width=4, font=("Comic Sans MS", 20), height=1)
        bnt.grid(row=row, column=column, sticky=W + E)
        l_text.append(bnt['text'])
        big_list.append(bnt)
        column += 1
        if column == 4:
            column = 0
            row += 1
    e1['bg'] = Theme['light']['e_bg']
    e2['bg'] = Theme['light']['e_bg']
    e3['bg'] = 'grey'
    e3['fg'] = 'black'

    root.config(bg='grey')
    butt.butt1()

main_menu = Menu(root)
root.config(menu=main_menu)
# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label="История", command=print_history)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=kalk_quit)
main_menu.add_cascade(label="Файл", menu=file_menu)
# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label="Light", command=lambda: change_theme_2('light'))
help_menu_sub.add_command(label="Dark", command=lambda: change_theme_1('dark'))
help_menu.add_cascade(label="Темы", menu=help_menu_sub)
help_menu.add_command(label="О программе", command=about_program)
main_menu.add_cascade(label="Разное", menu=help_menu)

root.mainloop()