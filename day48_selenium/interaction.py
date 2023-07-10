from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def wiki():
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    
    title = driver.find_element(By.CSS_SELECTOR, 'div #articlecount a')
    title.click()

    search = driver.find_element(By.NAME, 'search')
    search.send_keys("Vedant")
    search.send_keys(Keys.ENTER)
    
    while(True):
        pass


def signup():
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
    
    fname = driver.find_element(By.NAME, 'fName')
    fname.send_keys("Vedant")
    fname.send_keys(Keys.ENTER)

    lname = driver.find_element(By.NAME, 'lName')
    lname.send_keys("Bhawnani")
    lname.send_keys(Keys.ENTER)

    mail = driver.find_element(By.NAME, 'email')
    mail.send_keys("asldkf@gmail.com")
    mail.submit()

def twitter():
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    URL = "https://twitter.com/compose/tweet"
    driver.get(URL)
    time.sleep(6)
    login_email = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    login_email.send_keys("vedant.bhawnani@gmail.com")
    login_email.send_keys(Keys.ENTER)
    time.sleep(3)
    # num_text = driver.find_element(By.XPATH, '//*[@id="modal-header"]/span/span')
    # num_textt = num_text.text
    # if :
    try:
         number = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
         number.send_keys("7021212224" + Keys.ENTER)
    except:
        print("error")      
        password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys("vedant2003" + Keys.ENTER)
    time.sleep(3)
    try:
        password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys("vedant2003" + Keys.ENTER)
    except:
         print("Password error")
    while True:
            pass
twitter()