import requests
from bs4 import BeautifulSoup

# res = requests.get("http://google.com")
# res.raise_for_status()

# print("resposne code: ", res.status_code)

# print(len(res.text)) # number html text in res
# print(res.text)

# with open("mygoogle.html", "w", encoding="utf-8") as f:
#     f.write(res.text)


url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())

# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("span", attrs={"class": "Ntxt_menu_genre"}))
# print(soup.find(attrs={"class" : "Ntxt_challenge_comic"}))

# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print(rank1.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank2, rank3)

# rank_2 = rank3.previous_sibling.previous_sibling
# print(rank_2)

# print("*******parent: ******",rank1.parent)
# rank1.find_next_sibling("li")

# fav = soup.find("a", text="달콤살벌한 부부-12화")
# print(fav)

cartoons = soup.find_all("a", attrs={"class": "title"})

for cartoon in cartoons:
    print(cartoon.get_text())