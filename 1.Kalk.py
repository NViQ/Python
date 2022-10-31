from tkinter import *
from tkinter import ttk

root = Tk()
root.title('УмножноСложитель')
root.iconbitmap('16.ico')
root.geometry('360x400+600+100')
root.resizable(False, False)
root.config(bg='grey')



# n1, k1 = float(input(f'Введите первое число: ')), float(input(f'Введите второе число: '))
# print(f'Выберите функцию в табличке...')


def clicked():
    if y1 == 170:
        e1.delete(0, END)
        n1 = int(e2.get())
        k1 = int(e3.get())
        e1.insert(END, f' {e2.get()} + {e3.get()} = {n1+k1};')
    else:
        clicked6()
    # print(f'Значит выбрал сложение, Ваш результат: {n1} + {k1} = {n1+k1}')

def clicked1():
    e1.delete(0, END)
    n1 = int(e2.get())
    k1 = int(e3.get())
    e1.insert(END, f' {e2.get()} - {e3.get()} = {n1 - k1};')
    # print(f'Значит выбрал вычитание, Ваш результат: {n1} - {k1} = {n1-k1}')

def clicked2():
    e1.delete(0, END)
    n1 = int(e2.get())
    k1 = int(e3.get())
    e1.insert(END, f' {e2.get()} * {e3.get()} = {n1 * k1};')
    # print(f'Значит выбрал умножение, Ваш результат: {n1} * {k1} = {n1*k1}')

def clicked3():
    e1.delete(0, END)
    n1 = int(e2.get())
    k1 = int(e3.get())
    n2 = n1/k1
    e1.insert(END, f' {e2.get()} / {e3.get()} = {round(n2,2)};')
    # print(f'Значит выбрал деление, Ваш результат: {n1} / {k1} = {n1/k1}')
def clicked4():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

y1 = 170
def clicked5():
    global cli, y1
    y1 += 30
    e4 = Entry(root, width=20)
    e4.place(x=10, y=y1)



def clicked6():
    global e4, y1
    e1.delete(0, END)
    e4 = Entry(root, width=20)
    n1 = int(e2.get())
    k1 = int(e3.get())
    n2 = int(e4.get())
    e1.insert(END, f' {e2.get()} + {e3.get()} + {e3.get()} = {n1 + k1 + n2};')



l = Label(root, text="Результат:",font=("Comic Sans MS", 10), bg='grey')
l.place(x=10, y=90)
e1 = Entry(root, width=35)
e1.place(x=10, y=110)

l = Label(root, text="Первое число:",font=("Comic Sans MS", 10), bg='grey')
l.place(x=10, y=10)
e2 = Entry(root, width=20)
e2.place(x=10, y=30)
l = Label(root, text="Второе число:",font=("Comic Sans MS", 10), bg='grey')
l.place(x=10, y=50)
e3 = Entry(root, width=20)
e3.place(x=10, y=70)


# n1, k1 = int(input(f'Введите первое число: ')), int(input(f'Введите второе число: '))
# print(f'Выберите функцию в табличке...')

# '360x400
btn = Button(root, text='+', command=clicked, activebackground='green', width=4, font=("Comic Sans MS", 20), height=1)
btn.place(x=285, y=10)
btn1 = Button(root, text='-', command=clicked1, activebackground='green', width=4, font=("Comic Sans MS", 20), height=1)
btn1.place(x=285, y=77)
btn2 = Button(root, text='*', command=clicked2, activebackground='green', width=4, font=("Comic Sans MS", 20), height=1)
btn2.place(x=285, y=144)
btn3 = Button(root, text='/', command=clicked3, activebackground='green', width=4, font=("Comic Sans MS", 20), height=1)
btn3.place(x=285, y=211)
btn4 = Button(root, text='C', command=clicked4, activebackground='green', width=4, font=("Comic Sans MS", 20), height=1)
btn4.place(x=285, y=278)
# btn = Button(root, text="Кнопка", command=clicked, font=("Comic Sans MS", 20))

# btn['font'] = 'Arial 15'
# btn.pack()
# btn1.pack()
# btn2.pack()
# btn3.pack()

btn5 = Button(root, text='доп. число', command=clicked5, activebackground='grey', font='Arial 10', height=1)
btn5.place(x=10, y=150)




root.mainloop()