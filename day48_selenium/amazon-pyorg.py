from selenium import webdriver
from selenium.webdriver.common.by import By

URL_com = 'https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/'
URL_in = 'https://www.amazon.in/Boat-Rockerz-550-Headphone-Aesthetics/dp/B0856HNLDK/?_encoding=UTF8&pd_rd_w=jXDog&content-id=amzn1.sym.a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_p=a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_r=TX24XR3H7E7S7932H0AN&pd_rd_wg=sMBK1&pd_rd_r=ea18f582-b90a-4164-b6d2-3cc7dc4d441b&ref_=pd_gw_ci_mcx_mr_hp_atf_m'

def amazon():
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(executable_path=chrome_driver_path) 


    driver.get(URL_in)
    price = driver.find_element(By.CLASS_NAME, 'a-price-whole')
    print(price.text)

def pyorg():
    URL = 'https://www.python.org/'
    upcoming = {}

    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get(URL)
    time = driver.find_elements(By.CSS_SELECTOR , 'div .event-widget .menu li time' )
    links = driver.find_elements(By.CSS_SELECTOR, 'div .event-widget .menu li a')
    for i in range(len(time)):
        upcoming[i] = {time[i].text : links[i].text}
    print(upcoming)
pyorg()
