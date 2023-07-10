import requests
import lxml
from bs4 import BeautifulSoup

header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'Accept-Language' : 'en-US,en;q=0.9',
}
URL_com = 'https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/'
URL_in = 'https://www.amazon.in/Boat-Rockerz-550-Headphone-Aesthetics/dp/B0856HNLDK/?_encoding=UTF8&pd_rd_w=jXDog&content-id=amzn1.sym.a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_p=a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_r=TX24XR3H7E7S7932H0AN&pd_rd_wg=sMBK1&pd_rd_r=ea18f582-b90a-4164-b6d2-3cc7dc4d441b&ref_=pd_gw_ci_mcx_mr_hp_atf_m'
r = requests.get(url=URL_com, headers= header)
data = r.text

soup = BeautifulSoup(data, 'lxml')

price = soup.find('span', class_ = 'a-offscreen').string

print(price)