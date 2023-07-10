from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def cookie():
    chrome_driver_path = 'C:\development\chromedriver_win32\chromedriver.exe'
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    
    # store = [store_items.text.split(" - ") for store_items in store_list]
    # store.remove(store[-1])
    # store.reverse()
    # print(store) 
    

    end_time = time.time() + 300
    store_list = driver.find_elements(By.CSS_SELECTOR, '.grayed b')
    while(end_time>time.time()):
        ttime = time.time() + 5
        while(ttime > time.time()):
            cookie = driver.find_element(By.ID, 'cookie').click()
        money = (driver.find_element(By.ID, 'money')).text
        if len(money)>3:
            money = money.replace(',', '')
        affordable = driver.find_elements(By.CSS_SELECTOR, '#store :not(.grayed) b')
        per_min = driver.find_element(By.ID, 'cps')
        if affordable:
            affordable[-1].click() 
            # if float(per_min.text.split(':')[1]) > 40:
            #     grandma = 0
            #     factory = 0
            #     if driver.find_element(By.CSS_SELECTOR, '#buyGrandma .amount').text:
            #         grandma = int((driver.find_element(By.CSS_SELECTOR, '#buyGrandma .amount')).text)
            #     if driver.find_element(By.CSS_SELECTOR, '#buyFactory .amount'):
            #         factory = int((driver.find_element(By.CSS_SELECTOR, '#buyFactory .amount')).text)
            #     if (grandma>10 or factory > 10) and affordable:
            #         affordable.remove(affordable[0])

                
    print(per_min.text)

cookie()