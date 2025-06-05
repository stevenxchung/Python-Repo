import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class WebScraper:
    def __init__(self, url, output_file="products.csv"):
        self.url = url
        self.output_file = output_file
        self.containers = []

    def fetch_page(self):
        with uReq(self.url) as uClient:
            page_html = uClient.read()
        self.page_soup = soup(page_html, "html.parser")

    def parse_products(self):
        self.containers = self.page_soup.findAll(
            "div", {"class": "item-container"}
        )

    def write_to_csv(self):
        with open(self.output_file, "w", encoding="utf-8") as f:
            headers = "Brand,Product Name,Shipping\n"
            f.write(headers)
            for container in self.containers:
                brand = container.div.div.a.img["title"]
                title_container = container.findAll(
                    "a", {"class": "item-title"}
                )
                product_name = title_container[0].text
                shipping_container = container.findAll(
                    "li", {"class": "price-ship"}
                )
                shipping = shipping_container[0].text.strip()
                print("Brand :" + brand)
                print("Product Name: " + product_name)
                print("Shipping: " + shipping)
                f.write(
                    f"{brand},{product_name.replace(',', '|')},{shipping}\n"
                )

    def run(self):
        self.fetch_page()
        self.parse_products()
        self.write_to_csv()
        input("Press any key to continue")


if __name__ == "__main__":
    url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
    scraper = WebScraper(url)
    scraper.run()
