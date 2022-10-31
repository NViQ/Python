from tkinter import *


root = Tk()
root.geometry('600x400+600+100')
root.config(bg='grey')

f_menu = Frame(root, bg="#1F252A", height=30)
f_text = Frame(root)
f_menu.pack(fill=X)
f_text.pack(fill=BOTH, expand=1)

l_menu = Label(f_menu, text='Menu', bg="#1F252A", fg="#C6DEC1", font=("Comic Sans MS", 10))
l_menu.place(x=10, y=5)

t = Text(f_text, bg = "#343D46", fg="#C6DEC1", padx=10, pady=10, wrap=WORD, insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10)
t.pack(fill=BOTH, expand=1, side=LEFT)

# bg = "#343D46" insertbackground="#EDA756", selectbackground="#4E5A65", width=30, spacing3=10
root.mainloop()