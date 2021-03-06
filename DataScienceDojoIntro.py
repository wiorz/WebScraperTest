from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import jsbeautifier

# Source tutorial: https://www.youtube.com/watch?v=XQgXKtPSzUI
# Title: Intro to Web Scraping with Python and Beautiful Soup
# @author Data Science Dojo and Ivan Ko

# ----code example 1----
    # look at the h1 header of the page
    # print("h1 is: ")
    # print(page_soup.h1)
    # example code: look at the p of the page
    # print("p is: ")
    # print(page_soup.p)
    # look at the span of the p of the page
    # print(page_soup.body.span)

# ----code example 2----
    # how many objects
    # print(len(containers))
    # print(containers[0])

# ----code example 3----
    # testing jsbeautifer
    # print(jsbeautifier.beautify(str(container.div)))
    # print()
    # print("-------------------")
    # to get to the a inside a div of a div
    # print(container.div.div.a)
    # print()
    # print("-------------------")    

def main():
    # looking into the desktop GPU page from newegg
    my_url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7709"
    print("Connecting " + my_url)
    # opening ip the connection and grab page
    uClient = uReq(my_url)
    # page_html is raw html
    page_html = uClient.read()
    uClient.close()
    # use BeautifulSoup to parse page_html and store as json object (probably)
    page_soup = soup(page_html, "html.parser")

    # ----code example 1----
    # See top

    # grabs each product
    containers = page_soup.findAll("div", {"class": "item-container"})
    print()
    print("-------------------")

    # ----code example 2----

    container = containers[0]

    # ----code example 3----

    # export result to a csv file
    filename = "products.csv"
    f = open(filename, "w")
    header = "Brand, Description, Shipping Cost\n"
    f.write(header)

    # the loop that prints the info we want
    for container in containers:
        brand = container.div.div.a.img["title"]
        title_container = container.findAll("a", {"class": "item-title"})
        product_name = title_container[0].text
        shipping_container = container.findAll("li", {"class": "price-ship"})
        shipping = shipping_container[0].text.strip()
        print("Brand: " + brand)
        print("Description: " + product_name)
        print("Shipping cost: " + shipping)
        print()

        # Important: replace the comas in the description string to avoid adding extra columns
        line = brand + "," + product_name.replace(",", "|") + "," + shipping + "\n"
        f.write(line)

    f.close()



main()
