# Import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
# To export file as csv and record date
import csv
from datetime import datetime

wait = input("This application will find the stock name, price, and time from the \nspecified quote page and write that information into a csv file. \n\nPress any key to continue")

# Specify the url
quote_page = "https://www.bloomberg.com/quote/VOO:US"

# Query the website and return the html to the variable "page"
page = urlopen(quote_page)

# Parse the html using BeautifulSoup and store in the variable "soup"
soup = BeautifulSoup(page, "html.parser")

# Take out the <div> of the name and get it's value
name_box = soup.find("h1", attrs={"class" : "name"})

# Here strip() is used to remove starting and trailing
name = name_box.text.strip()
print(name)

# Get the index price
price_box = soup.find("div", attrs={"class" : "price"})
price = price_box.text
print(price)

# Open a csv file with append, so old data will not be erased
with open("stockScraperIndex.csv", "w") as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([name, price, datetime.now()])
