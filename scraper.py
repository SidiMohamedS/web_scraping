#importation des packages
import requests
from bs4 import BeautifulSoup

def scrape_title(url):
    r = requests.get(url)
    bs = BeautifulSoup(r.content, 'html.parser')
    titre = bs.h1
    return titre

titre = scrape_title('https://www.octoparse.com/blog/web-data-extraction-2020')

print(titre)