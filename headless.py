import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()


url = "https://play.google.com/store/movies/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAQ%3D:S:ANO1ljJvXQM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYBA%3D%3D:S:ANO1ljK7jAA"

# res = requests.get(url)
# res.raise_for_status()



# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())


browser.get(url)

# browser.execute_script("window.scrollTo(0,2080)")



interval = 2
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)
    cur_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == cur_height:
        break

    prev_height = cur_height

print("scroll finished")
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class": "Vpfmgd"})

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()

    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "remove from the list")
        continue

    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.find("a", attrs={"class": "JC71ub"})["href"]

    print(f"title:{title}") 
    print(f"original:{original_price}") 
    print(f"discount:{price}") 
    print("link:", "https://play.google.com" + link) 
    print("-"*60)

browser.quit()


