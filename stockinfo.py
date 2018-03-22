import requests
from bs4 import BeautifulSoup
import urllib3

def main():
    url = "https://finance.yahoo.com/quote/GOOG/key-statistics?p=GOOG"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    print(soup.prettify())







main()
