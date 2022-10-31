from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import os.path


root = Tk()
root.title('Техники')
root.iconbitmap('тел.ico')
root.geometry("230x100+600+300")
root.resizable(False, False)
root.config(bg="#726F77")
with open("tehn.txt", encoding='utf-8') as f:
    text = f.read()

def poisk(arg):
        l = []
        for i in text.split():
            if i != '-':
                l.append(i)
        for n in l:
            if arg in n:
                e1.delete(0, END)
                e1.insert(END, f'{n}-{l[l.index(n)+1]}')
def dob(arg):
    f = open("tehn.txt", 'a', encoding='utf-8')
    msg = messagebox.askyesno(title='Откуда техник', message="Это Изет?")
    if msg:
        f.write(arg +' '+'-'+' '+'Изет'+'\n')
    else:
        f.write(arg +' '+'-'+' '+'Энф'+'\n')
    f.close()



l1 = Label(root, text='Номер:', bg="#1A191C", fg="#87848D")
l1.pack(fill=X)
e1 = Entry(root, font=("Comic Sans MS", 13), bg="#726F77")
e1.pack(fill=X)

bnt = Button(root, text='Определить', command=lambda: poisk(e1.get()), bg="#1A191C", fg="#87848D", activebackground="#453D57")
bnt.pack(fill=X, side=LEFT, padx=5)
bnt1 = Button(root, text='Очистить', command=lambda: e1.delete(0, END), bg="#1A191C", fg="#87848D", activebackground="#453D57")
bnt1.pack(fill=X, side=LEFT, padx=5)
bnt2 = Button(root, text='Добавить', command=lambda: dob(e1.get()), bg="#1A191C", fg="#87848D", activebackground="#453D57")
bnt2.pack(fill=X, side=LEFT, padx=5)

root.mainloop()

