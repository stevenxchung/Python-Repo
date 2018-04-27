# Import libraries
import pdb
import bs4
import requests
from bs4 import BeautifulSoup as soup

my_url = "https://www.amazon.com/s/ref=sr_pg_2?rh=k%3Ahot+sauce%2Cn%3A16310101%2Cn%3A6502765011&page=2&keywords=hot+sauce&ie=UTF8&qid=1524791074"

# Opens connections and grabs webpage
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
page_html = requests.get(my_url, headers=headers)

# HTML parsing
page_soup = soup(page_html.content, "lxml")

# Grab each product
containers = page_soup.findAll("div", {"class" : "s-item-container"})

# Define first container
container = containers[0]

# GET PRODUCT NAME
def get_product_name(container):
  # Look in the image container
  image_container = container.findAll("img", {"class" : "s-access-image cfMarker"})

  # Opening quotations in alt=""
  indexFirstQ = str(image_container).find("alt") + 4
  firstChar = indexFirstQ + 1
  # Closing quotations in alt=""
  indexSecQ = str(image_container).find("\"", indexFirstQ + 1)

  # Get the product name
  product_name = str(image_container)[firstChar:indexSecQ]
  print("Product Name: " + product_name)

  return product_name

def get_price_and_reviews(container):
    # Look in the span containing the product price
  span_class = container.findAll("span", {"class" : "a-offscreen"})
  print(span_class)

  # Look in the a tag containing the number of reviews
  reviews_a_tag = container.findAll("a", {"class" : "a-size-small a-link-normal a-text-normal"})
  print("Elements in reviews tag: " + str(len(reviews_a_tag)))
  print(reviews_a_tag)

  # If span_class is empty, skip a container
  if not (span_class and reviews_a_tag):
    next(room)

  # When span_class or reviews_a_tag is not empty
  else:
    # Get the product price
    if (span_class[0].text.find("$") != -1):
      product_price = span_class[0].text
    else:
      product_price = span_class[1].text

    # Get the number of product reviews
    product_reviews = reviews_a_tag[0].text.strip()

    print("Price " + product_price)
    print("Product Reviews: " + product_reviews)

  return product_price, product_reviews


# # Write to file
filename = "amazonHotSauces.csv"
f = open(filename, "w")
headers = "Product Name, Price, Reviews\n"
f.write(headers)

# Initialize iterator to use next()
room = iter(containers)
for container in room:

  print("\n##########\n\nElements in container: " + str(len(container)))

  # GET PRODUCT NAME
  get_product_name(container)

  ##### GET PRODUCT PRICE & PRODUCT REVIEWS #####
  get_price_and_reviews(container)

  #f.write(product_name.replace(",", "-") + "," + product_price + "," + product_reviews.replace(",", "") + "\n")

f.close()

input("Done! Press any key to continue")
