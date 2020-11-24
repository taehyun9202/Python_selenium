import requests
from bs4 import BeautifulSoup

url= "https://comic.naver.com/webtoon/list.nhn?titleId=602910&weekday=mon"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# episodes = soup.find_all("td", attrs={"class":"title"})

# title = episodes[0].a.get_text()
# print(title)

# link = episodes[0].a["href"]
# print("https://comic.naver.com" + link)

# for episode in episodes:
#     title = episode.a.get_text()
#     link = "https://comic.naver.com" + episode.a["href"]
#     print(title, link)


# cartoon rating
episodes = soup.find_all("div", attrs={"class":"rating_type"})
total_sum = 0
for episode in episodes:
    rate = episode.find("strong").get_text()
    total_sum += float(rate)

avg = total_sum / len(episodes)
print(avg)
