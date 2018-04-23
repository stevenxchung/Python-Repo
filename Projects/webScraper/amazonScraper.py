# Import libraries
import bs4
import requests
from bs4 import BeautifulSoup as soup

my_url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dgrocery&field-keywords=hot+suace"

# Opens connections and grabs webpage
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
page_html = requests.get(my_url, headers=headers)

# HTML parsing
page_soup = soup(page_html.content, "lxml")

# Grab each product
containers = page_soup.findAll("div", {"class" : "s-item-container"})

# Define first container
container = containers[0]

# Export file as html
# filename = "test.html"
# f = open(filename, "w")
# f.write(str(container))
# f.close()

# image_container = container.findAll("img", {"class" : "s-access-image cfMarker"})

# # Opening quotations in alt=""
# indexFirstQ = str(image_container).find("alt") + 4
# firstChar = indexFirstQ + 1

# # Closing quotations in alt=""r
# indexSecQ = str(image_container).find("\"", indexFirstQ + 1)

# print(str(image_container)[firstChar:indexSecQ])

# Write to file
filename = "amazonHotSauces.csv"
f = open(filename, "a")
headers = "Product Name, Price\n"
f.write(headers)

for container in containers:
  # Look in the image container
  image_container = container.findAll("img", {"class" : "s-access-image cfMarker"})
  # Opening quotations in alt=""
  indexFirstQ = str(image_container).find("alt") + 4
  firstChar = indexFirstQ + 1
  # Closing quotations in alt=""r
  indexSecQ = str(image_container).find("\"", indexFirstQ + 1)
  # Get the product name
  product_name = str(image_container)[firstChar:indexSecQ]

  # Look in the span
  span_class = container.findAll("span", {"class" : "a-offscreen"})

  # Get the product price
  if (span_class[0].text.find("$") != -1):
    product_price = span_class[0].text
  else:
    product_price = span_class[1].text

  print("Product Name: " + product_name)
  print("Price " + product_price)

  f.write(product_name.replace(",", "-") + "," + product_price + "\n")

f.close()
