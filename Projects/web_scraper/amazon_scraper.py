import requests
from bs4 import BeautifulSoup as soup


class Scraper:
    def __init__(self, filename="amazon_hot_sauces.csv"):
        self.filename = filename
        self.page_numbers = [2, 3, 4, 5, 6, 7, 8, 9]

        # Clear previous csv
        with open(self.filename, "w") as _:
            pass

    def write_to_file(self, containers, n):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"Page {n - 1}\n")
            f.write("Product Name, Price, Reviews\n")

            for container in containers:
                product_name = self.get_product_name(container)
                price_reviews = self.get_price_and_reviews(container)

                if not (product_name and price_reviews):
                    continue

                price, reviews = price_reviews
                f.write(
                    f"{product_name.replace(',', '-')},{price},{reviews.replace(',', '')}\n"
                )

        print(f"\nDone scraping page {n - 1}!")

    def get_product_name(self, container):
        image_container = container.find_all(
            "img", {"class": "s-access-image cfMarker"}
        )
        if not image_container:
            return None
        alt_text = image_container[0].get("alt", "").strip()
        print("Product Name:", alt_text)
        return alt_text

    def get_price_and_reviews(self, container):
        span_class = container.find_all("span", {"class": "a-offscreen"})
        reviews_a_tag = container.find_all(
            "a", {"class": "a-size-small a-link-normal a-text-normal"}
        )

        if not (span_class and reviews_a_tag):
            return None

        # Get the product price
        product_price = next(
            (span.text for span in span_class if "$" in span.text), None
        )
        if not product_price and len(span_class) > 1:
            product_price = span_class[1].text

        # Get the number of product reviews
        review_text = reviews_a_tag[0].text.strip()
        product_reviews = "0" if "Save" in review_text else review_text

        print("Price:", product_price)
        print("Product Reviews:", product_reviews)

        return product_price, product_reviews

    def scrape(self):
        for n in self.page_numbers:
            my_url = (
                f"https://www.amazon.com/s/ref=sr_pg_{n}"
                "?rh=k%3Ahot+sauce%2Cn%3A16310101%2Cn%3A6502765011"
                f"&page={n}&keywords=hot+sauce&ie=UTF8&qid=1524791074"
            )

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
            }
            response = requests.get(my_url, headers=headers)
            page_soup = soup(response.content, "lxml")

            containers = page_soup.find_all(
                "div", {"class": "s-item-container"}
            )
            if not containers:
                print(f"No containers found on page {n}")
                continue

            self.write_to_file(containers, n)


if __name__ == "__main__":
    test = Scraper()
    test.scrape()
