import requests
from bs4 import BeautifulSoup
from selenium import webdriver

web_driver_path = "C:\\Users\\matca\\Desktop\\webDraiver\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=web_driver_path)
url = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
driver.get(url)
basic_selector = ".lister-item-content .lister-item-header"
all_titles_temp = driver.find_elements_by_css_selector(f".lister-item-content .lister-item-header a")
all_ranking_temp = driver.find_elements_by_css_selector(f".lister-item-content .lister-item-header .lister-item-index")
all_years_temp = driver.find_elements_by_css_selector(f".lister-item-content .lister-item-header .lister-item-year")
all_descriptions_temp = driver.find_elements_by_css_selector(".lister-item-content .text-muted")
all_ratings_temp = driver.find_elements_by_css_selector(".lister-item-content .ratings-bar strong")
all_images = driver.find_elements_by_css_selector(".lister-item-image  a img")
# in all images i need to do i.get_attribute('src'))
all_titles = []
all_ranking = []
all_year = []
all_descriptions = []
all_ratings = []
for i in all_titles_temp:
    all_titles.append(i.text)
for i in all_ranking_temp:
    if (i.text[1]) == '.':
        all_ranking.append(i.text[0])
    else:
        all_ranking.append(i.text[0:2])
for i in all_years_temp:
    all_year.append(i.text[1:5])
count = 1
for i in all_descriptions_temp:
    if len(i.text) > 50:
        all_descriptions.append(i.text)
for i in all_ratings_temp:
    all_ratings.append(i.text)

print(len(all_images), len(all_titles), len(all_year), len(all_ratings), len(all_ranking),len(all_descriptions))
driver.close()
