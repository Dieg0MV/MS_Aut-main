from Ms_aut import *
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
        

def sincronizar():
    try:
      driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
      start_url = 'https://web.whatsapp.com'
      driver.get(start_url)
      wait = WebDriverWait(driver, 40)

      etiquetas = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/header/div/span/div/span/div[2]/div/span')))
      time.sleep(2)
      etiquetas.click()
      time.sleep(2)
      etiqueta = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[3]/header/header/div/span/div/span/div[2]/span/div/ul/li[8]/div')    
      time.sleep(2)
      etiqueta.click()
      time.sleep(2)
      etiquetaname = driver.find_elements(By.CLASS_NAME, '_ao3e')
      time.sleep(3)
      for i in etiquetaname:
        print(i.text)

        with open("data.json", "w") as file:
          file.write({"name":i.text})

        time.sleep(2)

        if i.text == "":
           
          break

        #etique = driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div/div/div/div/div[1]/div/div/div/div[2]/div[1]/div/span')
        #for i in ex
    except Exception as e:
      print("error", e)
    
    finally:
       driver.quit()

sincronizar()

def serchNick():
  data = 7