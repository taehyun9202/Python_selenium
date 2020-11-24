import requests
from bs4 import BeautifulSoup

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup
    
def scrape_weather():
    print("========== Weather Today ==========")
    url = "https://weather.com/weather/today/l/e55d3d7a89d43b8338e104cfab058fc9df6390a0698200f694a76a8fd3f2e5f6"
    soup = create_soup(url)
    current_temp = soup.find("span", attrs={"class": "CurrentConditions--tempValue--3KcTQ"}).get_text()
    current_weather = soup.find("div", attrs={"class": "CurrentConditions--phraseValue--2xXSr"}).get_text()
    max_temp = soup.find_all("div", attrs={"class": "WeatherDetailsListItem--wxData--23DP5"})[0].find_all("span")[0].get_text()
    min_temp = soup.find_all("div", attrs={"class": "WeatherDetailsListItem--wxData--23DP5"})[0].find_all("span")[1].get_text()
    humidity = soup.find("span", attrs={"data-testid":"PercentageValue"}).get_text().strip()
    sunrise = soup.find_all("p", attrs={"class":"SunriseSunset--dateValue--2nwgx"})[0].get_text()
    sunset = soup.find_all("p", attrs={"class":"SunriseSunset--dateValue--2nwgx"})[1].get_text()
    print("Sunrise: {}, Sunset: {}".format(sunrise, sunset))
    print("Current Weather: ", current_weather)
    print("Current: {}, Maximum: {}, Minimin {}".format(current_temp, max_temp, min_temp))
    print("Humidity: ", humidity)

# def scrape_headline():
#     print("========== Head Line ==========")
#     url = "https://www.cnn.com/"
#     soup = create_soup(url)

    

if __name__ == "__main__":
    scrape_weather()
    # scrape_headline()

