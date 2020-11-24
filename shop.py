import requests
from bs4 import BeautifulSoup
import re

for i in range(1, 10):
    print("page: ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken={}=4&backgroundColor=".format(i)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    # print(res.text)

    items = soup.find_all("li", attrs={"class": re.compile("search-product")})
    # print(items[0].find("div", attrs={"class": "name"}).get_text())

    for index, item in enumerate(items):
        name = item.find("div", attrs={"class": "name"}).get_text()
        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class":"rating"})
        if rate:
            rate = rate.get_text()
        else:
            rate = "no rate"
        num_rate = item.find("span", attrs={"class":"rating-total-count"})
        if num_rate:
            num_rate = num_rate.get_text()
            num_rate = num_rate[1:-1]
        else:
            num_rate = "no rate"
        
        link = item.find("a", attrs={"class": "search-product-link"})["href"]
        if rate != "no rate":
            if float(rate) == 5 and int(num_rate) >= 50:
                print(index, name, price, rate, num_rate, "https://www.coupang.com" + link)
                print("----------- --------------------")