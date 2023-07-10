from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def twitter():
    EMAIL = ""
    NUMBER = ""
    PaSSWORD = ""
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    URL = "https://twitter.com/compose/tweet"
    driver.get(URL)
    time.sleep(6)
    login_email = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    login_email.send_keys(EMAIL)
    login_email.send_keys(Keys.ENTER)
    time.sleep(3)
    # num_text = driver.find_element(By.XPATH, '//*[@id="modal-header"]/span/span')
    # num_textt = num_text.text
    # if :
    try:
         number = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
         number.send_keys(NUMBER + Keys.ENTER)
    except:
        print("error")      
        password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PaSSWORD + Keys.ENTER)
    time.sleep(3)
    try:
        password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys("vedant2003" + Keys.ENTER)
    except:
         print("Password error")
    time.sleep(3)

    # tweets = driver.find_element(By.CSS_SELECTOR("#Tweetstorm-tweet-box-0 > div.tweet-box-content > div.tweet-content > div.RichEditor.RichEditor--emojiPicker.is-fakeFocus > div.RichEditor-container.u-borderRadiusInherit > div.RichEditor-scrollContainer.u-borderRadiusInherit > div.tweet-box.rich-editor.is-showPlaceholder"))

    # tweets.click()
    # tweets.sendKeys("heys")
    
    driver.get(URL)
    
    # new_tweet = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[1]/div')
    # new_tweet.click()
    
    # new_tweet.send_keys("Hello Hi This tweet was sent through Selenium.")

    while True:
        pass
twitter()