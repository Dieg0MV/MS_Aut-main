from Ms_aut import *
def maps():
    try:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        start_url = 'https://www.google.com.mx/maps'
        driver.get(start_url)
        wait = WebDriverWait(driver, 40)

        bar_serch = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
        bar_serch.send_keys("helados")
        time.sleep(3)
        bar_serch.send_keys(Keys.ENTER)
        time.sleep(3)
        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'hfpxzc')))
        time.sleep(2)
        #items= driver.find_elements(By.CLASS_NAME, 'hfpxzc')
        #time.sleep(2)
        
        for n in items:
            time.sleep(2)
            n.click()
            print("next")
            time.sleep(4)
            nums = driver.find_element(By.XPATH,'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[7]/div[4]/button/div/div[2]/div[1]')
            time.sleep(3)
            if nums.text == "":
                time.sleep(2)
                pass
            else:
                print(nums.text)
                time.sleep(2)

    except Exception as e:
        print("error en ", e)

    finally:
       print("eso es todo")
       driver.close()

maps()
