from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

URL = 'https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.536739%2C%22east%22%3A-122.32992%2C%22south%22%3A37.707608%2C%22north%22%3A37.842914%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%7D'
FORM = 'https://forms.gle/2TZQ8ejgHWLYfSYq5'

def selen():    
    # print(links)
    chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    for i in range(len(addr)):
        driver.get(FORM)
        add = driver.find_element(By.CLASS_NAME, 'zHQkBf')
        add.click()
        add.send_keys(addr[i], Keys.TAB, cost[i], Keys.TAB, links[i])
        submit = driver.find_element(By.CLASS_NAME, 'NPEfkd').click()

    while True:
        pass  



header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Accept-Language' : 'en-US,en;q=0.9',
}

r = requests.get(url = URL, headers = header)
data = r.text 

soup = BeautifulSoup(data, 'lxml')

price = soup.find_all("div", class_ = 'gMDnGj')
cost = [cost.text for cost in price]
# print(cost)
anchor = soup.find_all('a', class_ = 'property-card-link') 
links = [element.get('href') for element in anchor]
# print(links)

for i in range(len(links)):
    if links[i][0:4] != 'http':
        links[i] = 'https://www.zillow.com' + links[i]

links = list(set(links))


addrs = [element.string for element in anchor]
addr = addrs[::2]
# print(addr)

selen()