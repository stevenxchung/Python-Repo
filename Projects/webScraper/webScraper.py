# Import libraries
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"

# Opens connections and grabs webpage
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html, "html.parser")

# Grab each product
containers = page_soup.findAll("div", {"class" : "item-container"})

# Write to file
filename = "products.csv"
f = open(filename, "w")
headers = "Brand, Product Name, Shipping\n"
f.write(headers)

# Define first container
container = containers[0]

for container in containers:
  brand = container.div.div.a.img["title"]

  title_container = container.findAll("a", {"class" : "item-title"})
  product_name = title_container[0].text

  shipping_container = container.findAll("li", {"class" : "price-ship"})
  shipping = shipping_container[0].text.strip()

  print("Brand :" + brand)
  print("Product Name: " + product_name)
  print("Shipping: " + shipping)

  f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()

wait = input("Press any key to continue")
