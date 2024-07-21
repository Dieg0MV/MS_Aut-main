from tkinter import ttk
from tkinter import *
from Ms_aut import MSsingle

root = Tk()
root.config(width=500, height=400)
frm = ttk.Frame(root, padding=10)
frm.grid()
def mss():
    MSsingle()

ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="new menssage", command=mss).grid(column=1, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=1)
root.mainloop()

