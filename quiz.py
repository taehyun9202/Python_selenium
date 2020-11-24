import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

# browser = webdriver.Chrome()
url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%E3%85%8E&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

sales = soup.find("tbody").find_all("tr")

for index, sale in enumerate(sales):
    deal = sale.find("td", attrs={"class": "col1"}).find("div", attrs={"class": "txt_ac"}).get_text()
    width = sale.find("td", attrs={"class": "col2"}).find("div", attrs={"class": "txt_ac"}).get_text()
    price = sale.find("td", attrs={"class": "col3"}).find("div", attrs={"class": "txt_ac"}).get_text()
    apt = sale.find("td", attrs={"class": "col4"}).find("div", attrs={"class": "txt_ac"}).get_text()
    floor = sale.find("td", attrs={"class": "col5"}).find("div", attrs={"class": "txt_ac"}).get_text()
    print("---------{}----------".format(index+1))
    print("deal: ", deal)
    print("width: ", width)
    print("price: ", price)
    print("apt: ", apt)
    print("floor: ", floor)

