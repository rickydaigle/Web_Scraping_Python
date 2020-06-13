#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import webbrowser

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

def check_walmart(site_name, url):

    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")
    
    product = soup.find("h1", class_="prod-ProductTitle font-normal").get_text().strip()
    stock = soup.find("div", class_="fulfillment-text").get_text().strip()
    price1 = soup.find("span", class_="price-characteristic").get_text().strip()
    price2 = soup.find("span", class_="price-mark").get_text().strip()
    price3 = soup.find("span", class_="price-mantissa").get_text().strip()

    webbrowser.open(url, new=2)

    print(site_name + ": " + product)
    print("\tPrice: $" + str(price1) + str(price2) + str(price3))
    print("\tStock: " + stock)
    print()
    print("If browser doesn't open automatically, copy/paste this into your browser: " + str(url))
    print("*" * 45)

def check_bjs(site_name, url):

    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")

    product = soup.find("h1", class_="product-title-name").get_text().strip()
    price = soup.find("span", class_="price-display").get_text().strip()

    webbrowser.open(url, new=2)

    print(site_name + ": " + product)
    print("\tPrice: " + str(price))
    print("\tStock: Check manually - could not parse!")
    print()
    print("If browser doesn't open automatically, copy/paste this into your browser: " + str(url))
    print("*" * 45)

def check_sams(site_name, url):

    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, "html.parser")

    product = soup.find("div", class_="sc-product-header-title-container").get_text().strip()
    price1 = soup.find("span", class_="Price-characteristic").get_text().strip()
    price2 = soup.find("span", class_="Price-mark").get_text().strip()
    price3 = soup.find("span", class_="Price-mantissa").get_text().strip()

    webbrowser.open(url, new=2)

    print(site_name + ": " + product)
    print("\tPrice: $" + str(price1) + str(price2) + str(price3))
    print("\tStock: Check manually - could not parse!")
    print()
    print("If browser doesn't open automatically, copy/paste this into your browser: " + str(url))
    print("*" * 45)

def main():

    print("Checking status...")
    print()
    print("*" * 45)
##    check_page("Amazon", "https://www.amazon.com/Scott-Sheets-Toilet-Paper-Tissue/dp/B07BQV5RWW/ref=sr_1_1?crid=3RYITJNVOPM9H&dchild=1&keywords=scott+toilet+paper&qid=1586196936&sprefix=scott+%2Caps%2C193&sr=8-1")
    check_walmart("WalMart", "https://www.walmart.com/ip/Scott-1000-Toilet-Paper-30-Rolls-30-000-Sheets/922074920")
##    check_page("Target", "websiteURL")
    check_bjs("BJ's Wholesale", "https://www.bjs.com/product/scott-1100-sheets-1-ply-bath-tissue-36-pk/3000000000000190611")
    check_sams("Sam's Club", "https://www.samsclub.com/p/scott-bath-bonus-pk-36-rolls-1000-sheets/prod11320181?xid=plp_product_1_1")
    print()
    check = input("Press 'Enter' to exit...")
    print()

if __name__ == "__main__":
    main()


