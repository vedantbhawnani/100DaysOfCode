import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL = "https://www.linkedin.com/jobs/search/?currentJobId=3488156015&f_AL=true&f_JT=I&f_WT=2&keywords=python%20developer&refresh=true"
USERNAME = "vedant.bhawnani@gmail.com"
PASS = "Vedant25"

def prog():
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    driver.get(URL)

    login = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]').click()

    time.sleep(1)

    user_field = driver.find_element(By.ID, 'username')
    user_field.send_keys(USERNAME)

    pass_field = driver.find_element(By.ID, 'password')
    pass_field.send_keys(PASS)

    signin = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
    # first = driver.find_elements(By.CSS_SELECTOR, 'a .disabled .ember-view .job-card-container__link .job-card-list__title')
    time.sleep(15)
    first = driver.find_elements(By.CLASS_NAME, 'job-card-list__title')
    print(first)
    for n in first:
        print(n.get_attribute("href"))
    # while True:
    #     pass


prog()