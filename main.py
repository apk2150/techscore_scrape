#find number of students registered on each team
import requests
from bs4 import BeautifulSoup
import csv
#https://realpython.com/beautiful-soup-web-scraper-python/
SEASON="s23"
URL = "https://scores.collegesailing.org/schools/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="page-content")
all_schools = results.find_all("td", class_="schoolname")
# print(results.prettify())
file_name="roster_sizes"+SEASON+".csv"
with open(file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['school_name', 'roster_size'])
    for school in all_schools:
        # print(school, end="\n" * 2)
        link=school.find("a")
        school_name= link.text
        school_roster_url="https://scores.collegesailing.org"+link["href"]+SEASON+"/roster/"
        # print(school_roster_url)
        new_page = requests.get(school_roster_url)
        new_soup = BeautifulSoup(new_page.content, "html.parser")
        header=new_soup.find(id="content-header")
        roster_size = header.find_all('span', class_="page-info-value")
        try:
            # print(school_name+","+roster_size[-1].text)
            writer.writerow([school_name, roster_size[-1].text])
        except:
            writer.writerow([school_name, ''])

