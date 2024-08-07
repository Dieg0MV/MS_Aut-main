from tkinter import ttk
from tkinter import *
from Ms_aut import *
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService



root = Tk()
root.title("MS_AUT")
root.geometry("600x500")
frm = ttk.Frame(root, padding=10)
frm.grid()

def send():
    message = message_text.get("1.0", "end-1c")
    filename = file_path.get()
    
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    start_url = 'https://web.whatsapp.com'
    driver.get(start_url)
    wait = WebDriverWait(driver, 30)
    
    excelFile = xlrd.open_workbook(filename)
    sheet1 = excelFile.sheet_by_index(0)
    for i in range(1, sheet1.nrows):    
        numeros = sheet1.cell_value(rowx=i, colx=1)
        if not numeros:
            print("listo")
            break
        file_s = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
        time.sleep(5)
         
        file_s.send_keys(int(numeros))
        time.sleep(1)
        file_s.send_keys(Keys.ENTER)
        # Esperar unos segundos para asegurarse de que se haya abierto la conversació
        time.sleep(2)
    
        chat_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

        # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
        time.sleep(1)
        message = message
        chat_box.send_keys(message)
        chat_box.send_keys(Keys.ENTER)
        time.sleep(5)
                
        # Hacer clic en el botón de adjuntar archivo
        attach_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')))        
        attach_button.click()


def select_file():
    file_path.set(filedialog.askopenfilename())


ttk.Label(frm, text="Ingresa tu mensaje").grid(column=0, row=2, pady=(10, 0))
message_text = Text(frm, height=10, width=40)
message_text.grid(column=0, row=2, columnspan=4, pady=(5, 10))

ttk.Button(frm, text="Seleccionar archivo de Excel", command=select_file).grid(column=4, row=1)
file_path = StringVar()

ttk.Button(frm, text="Send", command=send).grid(column=0, row=4)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()

