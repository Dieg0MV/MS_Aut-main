from tkinter import ttk
from tkinter import *
from Ms_aut import *

root = Tk()
root.config(width=500, height=400)
frm = ttk.Frame(root, padding=30)
frm.grid()
def mss():
    MSsingle

ttk.Label(frm, text="MS_AUT").grid(column=0, row=0)
ttk.Button(frm, text="new menssage", command=mss).grid(column=1, row=1)

ttk.Button(frm, text="agregar imagen", command=filedialog.askopenfilename()).grid(column=2, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=2)
root.mainloop()

