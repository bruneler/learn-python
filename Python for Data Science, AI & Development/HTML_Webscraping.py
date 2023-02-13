from bs4 import BeautifulSoup
import requests
## import pandas as pd  # für Interaktion mit CSV files und XML
# import json  # für Interaktoin mit JSON Files
# import xml.etree.ElementTree as etree
html = "<!DOCTYPE html><html>" \
       "<head>" \
       "<title>Page title</title>" \
       "</head>" \
       "<body><h3><b id='boldest'>Lebron James</b></h3>" \
       "<p> Salary: $ 92,000,000</p>" \
       "<h3> Stephen Curry</h3>" \
       "<p> Salary: $85,000, 000 </p>" \
       "<h3> Kevin Durant </h3>" \
       "<p> Salary: $73,200, 000</p>" \
       "</body>" \
       "</html>"


soup = BeautifulSoup(html, 'html5lib')  # Parse the site to the bs4 lib and create the object as a nested structure

# Wir können mit soup objekt auf die html tags zugreifen.
tag_object = soup.title
print(tag_object)

tag_object = soup.h3
print(tag_object)  # Wenn es mehrere h3 elemente gibt, wird das Erste ausgewählt.

# Wenn wir uns die Seite als Baumstruktur vorstellen, ist das b-Tag ein child-Tag von h3.
tag_child = tag_object.b
print(tag_child)
# Das übergeordnete Element heisst Parent
parent_tag = tag_child.parent
print(parent_tag)
# Das nächste Element auf der gleichen Stufe "Next-sibling"
sibling_1 = tag_object.next_sibling
print(sibling_1)
sibling_2 = sibling_1.next_sibling
print(sibling_2)

# Durch den String navigieren
print(tag_child.attrs)

# Wir können mit Beautiful Soup direk auf den String zugreifen.
print(tag_child.string)

# mit Find all Methode elemente filtern. Gibt alle elemente mit h3 Tags aus.


soup_h3 = soup.find_all(name='h3')
print(soup_h3)

# Auf einzelne Elemente dieser Filterliste zugreifen
first_element = soup_h3[0]
print(first_element)
print(first_element.b)  # Auf Child-Tag zugreifen
print("\n\n\n\n")

# Mit for-schleife durch
for i, element in enumerate(soup_h3):
    print("Durchgang:", i, element)
    childs = element.find_all("b")
    print(childs)


###  Dummy Programm ###
URL = "https://sbb.ch"
page = requests.get(URL).text
# Kreirt ein Beautiful Soap Objekt
soup = BeautifulSoup(page, "html.parser")
# Pulls alle Instanzen mit <a> tag
founded_links = soup.find_all('a')

# Bereinigt Daten von allen allen Tags
for links in founded_links:
    linktext = links.contents[0]
    fullLink = links.get('href')
    print("Link Text:", linktext)
    print(fullLink)


