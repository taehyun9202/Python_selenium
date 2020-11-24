import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020):
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images =  soup.find_all("img", attrs={"class": "thumb_img"})
    for index, image in enumerate(images):
        img_url = image["src"]
        if img_url.startswith("//"):
            img_url = "https:" + img_url

        img_res = requests.get(img_url)
        img_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, index+1), "wb") as f:
            f.write(img_res.content)
        

        if index >= 4:
            break;