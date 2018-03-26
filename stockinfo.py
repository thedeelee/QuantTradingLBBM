import requests
from bs4 import BeautifulSoup
import urllib3
import csv

def main():

    """https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL
    url = "https://finance.yahoo.com/quote/GOOG/key-statistics?p=GOOG"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    gu = soup.prettify())
    """

    ticker_name = getTicker()
    print (ticker_name)



def getTicker():
    with open('companylist.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        tickers = []
        names = []
        ticker_name = []
        for row in readCSV:
            ticker = row[0]
            name = row[1]

            tickers.append(ticker)
            names.append(name)

        for i in range(len(tickers)):
            ticker_name.append(tickers[i] + " , " + names[i])

        return ticker_name










main()
