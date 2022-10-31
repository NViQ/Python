from tkinter import *
from tkinter import ttk
from les5_dz import Colors

root = Tk()
root.title('Все цвета радуги')
root.iconbitmap('1.ico')
root.geometry('180x220+600+100')
root.config(bg='grey')

l_text = Label(root, bg='grey', fg='white', justify=CENTER)
l_text.pack(fill=X)
e1 = Entry(root, bg='grey', fg='white', justify=CENTER)
e1.pack(fill=X)

colors1 = {
    "#ff0000": "Красный",
    "#ff7d00": "Оранжевый",
    "#ffff00": "Желтый",
    "#00ff00": "Зеленый",
    "#007dff": "Голубой",
    "#0000ff": "Синий",
    "#7d00ff": "Фиолетовый",
}

butt = Colors(root, e1, l_text, colors1)
butt.run()

root.mainloop()



'''
Напишите программу, состоящую из семи кнопок, цвета которых соответствуют цветам радуги. При нажатии на ту или иную кнопку в текстовое поле должен вставляться код цвета, а в метку – название цвета.
#ff0000: Красный
#ff7d00: Оранжевый
#ffff00: Желтый
#00ff00: Зеленый
#007dff: Голубой
#0000ff: Синий
#7d00ff: Фиолетовый
'''

