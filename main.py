#find number of students registered on each team
import requests
from bs4 import BeautifulSoup
#https://realpython.com/beautiful-soup-web-scraper-python/
SEASON="f23"
URL = "https://scores.collegesailing.org/schools/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="page-content")
all_schools = results.find_all("td", class_="schoolname")
# print(results.prettify())
for school in all_schools:
    print(school, end="\n" * 2)
    link=school.find("a")
    school_name= link.text
    school_roster_url="https://scores.collegesailing.org"+link["href"]+SEASON+"/roster/"
    print(school_roster_url)
    # new_page = requests.get(URL)
    # new_soup = BeautifulSoup(page.content, "html.parser")
    # links = new_soup.find_all('a', text='text to find')
