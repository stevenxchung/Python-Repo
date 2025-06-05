from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime


class StockScraper:
    def __init__(self, url, output_file="stock_scraper_index.csv"):
        self.url = url
        self.output_file = output_file
        self.name = None
        self.price = None

    def fetch_data(self):
        page = urlopen(self.url)
        soup = BeautifulSoup(page, "html.parser")
        name_box = soup.find("h1", attrs={"class": "name"})
        price_box = soup.find("div", attrs={"class": "price"})
        if name_box and price_box:
            self.name = name_box.text.strip()
            self.price = price_box.text.strip()
        else:
            raise ValueError("Could not find stock name or price on the page.")

    def save_to_csv(self):
        with open(self.output_file, "w", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.name, self.price, datetime.now()])

    def run(self):
        input(
            "This application will find the stock name, price, and time from the \nspecified quote page and write that information into a csv file. \n\nPress any key to continue"
        )
        self.fetch_data()
        print(self.name)
        print(self.price)
        self.save_to_csv()


if __name__ == "__main__":
    scraper = StockScraper("https://www.bloomberg.com/quote/VOO:US")
    scraper.run()
