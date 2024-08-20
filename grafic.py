from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from Ms_aut import *
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService



def select_file():
    file_path.set(filedialog.askopenfilename(
        filetypes=[("Archivos de Excel", "*.xls;*")]
    ))
    # Actualizar el contenido del label con el archivo seleccionado
    file_label.config(text=file_path)
def img_file():
    image_path.set(filedialog.askopenfilename(
        filetypes=[("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")]

    ))
    

def send():
    global image_path    
    message = message_text.get("1.0", "end-1c")
    filename = file_path.get()
    image_path = image_path.get()
    
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    start_url = 'https://web.whatsapp.com'
    driver.get(start_url)
    wait = WebDriverWait(driver, 30)
    
    excelFile = xlrd.open_workbook(filename)
    sheet1 = excelFile.sheet_by_index(0)
   
    print("la imagen ", image_path) 
   
    
    for i in range(1, sheet1.nrows):    
        numeros = sheet1.cell_value(rowx=i, colx=1)
        if not numeros:
            print("listo")
            break
        file_s = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p')))
        time.sleep(3)
         
        file_s.send_keys(int(numeros))
        time.sleep(4)
        file_s.send_keys(Keys.ENTER)
        # Esperar unos segundos para asegurarse de que se haya abierto la conversació
        time.sleep(2)
    
        chat_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
        # Esperar unos segundos para que el mensaje se envíe antes de pasar al siguiente número
        if image_path == "":
            time.sleep(2)
            message = message
            chat_box.send_keys(message)
            chat_box.send_keys(Keys.ENTER)
            time.sleep(3)
        else:
            attach_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span')))        
            attach_button.click()
            # Seleccionar la opción de enviar una imagen
            image_option = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
            image_option.send_keys(image_path)
            time.sleep(2)
            enviar = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div')
            message = message
            chat_box.send_keys(message)
            chat_box.send_keys(Keys.ENTER)
            enviar.send_keys(Keys.ENTER)
            time.sleep(3)
    

root = Tk()
root.title("MS_AUT")
root.geometry("600x500")
frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Ingresa tu mensaje").grid(column=0, row=2, pady=(10, 0))
message_text = Text(frm, height=10, width=40)
message_text.grid(column=0, row=2, columnspan=4, pady=(5, 10))
image_path = StringVar()
file_path = StringVar()

ttk.Button(frm, text="Seleccionar Excel", command=select_file).grid(column=5, row=2)
file_label = ttk.Label(frm, text="")
file_label.grid(column=0, row=1, columnspan=4)

ttk.Button(frm, text="Seleccionar Imagen", command=img_file).grid(column=5, row=1)
ttk.Button(frm, text="Send", command=send).grid(column=0, row=4)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()

