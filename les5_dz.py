from tkinter import *
from tkinter import ttk

class Colors:
    def __init__(self, root, entr, labl, dirt):
        self.dirt = dirt
        self.root = root
        self.entr = entr
        self.labl = labl

    def creat_butt(self):
        def clicked(text_color, hex_color):
            self.labl['text'] = text_color
            self.entr.delete(0, END)
            self.entr.insert(0, hex_color)

        for k, v in self.dirt.items():
            Button(self.root, bg=k, command=lambda text=v, hex=k: clicked(text, hex), activebackground=k).pack(fill=X)
    def run(self):
        self.creat_butt()