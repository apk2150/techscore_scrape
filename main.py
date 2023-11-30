
import requests
from bs4 import BeautifulSoup
#https://realpython.com/beautiful-soup-web-scraper-python/

URL = "https://scores.collegesailing.org/schools/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="page-content")
job_elements = results.find_all("td", class_="schoolname")
# print(results.prettify())
for job_element in job_elements:
    print(job_element, end="\n"*2)