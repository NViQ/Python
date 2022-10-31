from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter import filedialog
import os
import os.path
from datetime import datetime
import shutil
import time
from tqdm import tqdm
from tkinter import Toplevel





root = Tk()
root.title('Распределитель')
root.geometry("500x160+600+300")
root.resizable(False, False)
root.config(bg="#726F77")

def dir_path():
    dir_path1 = filedialog.askdirectory()
    n = dir_path1.replace('/', '\\')
    e1.delete(0, END)
    e1.insert(0, n)
    bnt1.config(text='Нажмите и ожидайте окончания...')

def raspred(get_path):
    path = get_path
    dir_list = []
    if path:
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    try:
                        path_file = os.path.join(root, file)
                        shutil.move(path_file, path)
                    except shutil.Error:
                        continue
                dir_list.append(root)
                for root in dir_list[::-1]:
                    try:
                        if not os.listdir(root):
                            os.rmdir(root)
                    except FileNotFoundError:
                        continue
            fdpaths = [path+"/"+fd for fd in os.listdir(path)]
            date_list=[]
            for fdpath in tqdm(fdpaths):
                statinfo = os.stat(fdpath)
                mod_date = datetime.fromtimestamp(statinfo.st_mtime).strftime("%d-%m-%Y")
                date_list.append(mod_date)
                for i in date_list:
                    for m in date_list:
                        if i == m:
                            if not os.path.isdir(f'{path}/{mod_date}'):
                                try:
                                    os.mkdir(f'{path}/{mod_date}')
                                except shutil.Error:
                                    continue
                shutil.move(fdpath, f'{path}/{mod_date}')
            messagebox.showinfo('Success', 'Сортировка выполнена успешно')
            bnt1.config(text='Распределить')
            e1.delete(0, END)
        except FileNotFoundError:
            messagebox.showwarning('Warning', 'Указан недопустимый адрес директории')
            e1.delete(0, END)
    else:
        messagebox.showwarning('Warning', 'Укажите директорию для распределения')

frame = Frame(root, bg="#1A191C", bd=5)
frame.pack(pady=10, padx=10, fill=X)

l1 = Label(frame, text='Укажите адрес папки:', bg="#1A191C", fg="#87848D", anchor='w')
l1.pack(fill=X)
e1 = Entry(frame, font=("Comic Sans MS", 15), bg="#726F77")
e1.pack(side=LEFT, ipady=2, expand=True, fill=X)

bnt = Button(frame, text='Выбрать папку', command=dir_path, bg="#1A191C", fg="#87848D", activebackground="#453D57")
bnt.pack(side=LEFT, padx=5, expand=True)

bnt1 = Button(root, text='Распределить', command=lambda: raspred(e1.get()), bg="#1A191C", fg="#87848D", activebackground="#FFEF00", width=4, font=("Comic Sans MS", 17),height=1)
bnt1.pack(fill=X, padx=10, pady=5)


root.mainloop()
