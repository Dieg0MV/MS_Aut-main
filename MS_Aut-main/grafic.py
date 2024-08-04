from tkinter import ttk
from tkinter import *
from Ms_aut import *
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

root = Tk()
root.config(width=500, height=400)
frm = ttk.Frame(root, padding=30)
frm.grid()

def send():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    start_url = 'https://web.whatsapp.com'
    driver.get(start_url)
    wait = WebDriverWait(driver, 30)
    

ttk.Label(frm, text="MS_AUT").grid(column=0, row=0)
ttk.Button(frm, text="new menssage", command=MSsingle).grid(column=2, row=1)
 
ttk.Button(frm, text="agregar imagen", command=filedialog.askopenfilename()).grid(column=3, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=4)
root.mainloop()

