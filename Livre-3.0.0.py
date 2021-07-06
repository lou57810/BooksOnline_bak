import requests
from bs4 import BeautifulSoup
import csv
import urllib
from urllib.parse import urljoin
#import pandas as pd

# Adresse de la catégorie (ici catégorie "defaut": 8 pages)
url = 'http://books.toscrape.com/catalogue/category/books/romance_8/index.html'

# Liste des url des livres dans les pages de la catégorie
listeUrlLivres = []

# Fonction récupérant l'adresse des livres
def appendListe(url, listeUrlLivres):
    urlPage = requests.get(url)
    if urlPage.ok:
        soup = BeautifulSoup(urlPage.text, 'html.parser')
        
    balise_livre = soup.findAll('article', {'class': 'product_pod'})        
    for article in balise_livre:
        a = article.find('a')
        link = a['href']
        link = link[8:len(link)]
        listeUrlLivres.append('http://books.toscrape.com/catalogue' + link)

urlPage = requests.get(url)
if urlPage.ok:
    soup = BeautifulSoup(urlPage.text, 'html.parser')

# Récupération du nombre de livres
nbrLivres = (soup.find('form').find('strong')).text
nbrLivres = int(nbrLivres)
print('Nombre de livres: ', nbrLivres)
    
if ((nbrLivres%20)>0):
    nbrPage = int((nbrLivres/20)+1)
    print('Nombre de pages: ', nbrPage)
        
if (nbrPage == 1):
    appendListe(url, listeUrlLivres)
        
else:
    appendListe(url, listeUrlLivres)
    
    url_base = url[0:(len(url) -10)]
    
    i = 2
    while i <= nbrPage:
        linkPage = 'page-' + str(i) + '.html'
        url = url_base + linkPage        
        
        appendListe(url, listeUrlLivres)
        i += 1

dataBook = {}
rows = []
labels = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'prod_description', 'category', 'review_rating', 'image_url']

try:    
    with open('dataBookCat.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        #for elem in dict_arr:
            #writer.writerow(elem)
except IOError:
    print("I/O error")

for elt in listeUrlLivres:
    url = str(elt)
    urlPage = requests.get(url)
    soup = BeautifulSoup(urlPage.text, 'html.parser')
    all_books = soup.find_all("article", class_ = "product_pod")
    for book in all_books:
        # url de chaque livre
        h3 = book.h3.find("a")["href"]
        # url absolue
        link = urljoin(url, h3)
        page = urllib.request.urlopen(link)
    
    tdiv = soup.find('table', class_='table table-striped')
    tds = tdiv.find_all('td')
    
    upc = tds[0].text        
    
    titre = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')    
    
        
    price_ttc = tds[3].text
    price_ttc = price_ttc[1:len(price_ttc)]
        
    price_ht = tds[2].text
    price_ht = price_ht[1:len(price_ht)]
            
    numAv = tds[5].text
    
    try:
        prod_description = soup.find("div", class_= "sub-header", id="product_description").h2.find_next().text
    except AttributeError:
        prod_description = None
        
    liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
    category = liste_a[2].text    
    
    reviewRating = tds[6].text
    
    # image
    img_url = book.a.img["src"]
    img_url = urljoin(url, img_url)
    '''    
    img_url = soup.find('div',{'id': 'product_gallery'}).find('img')
    img_url = str(img_url)    
    #img_url = urljoin(link, img_url)
    img_url = img_url[51:len(img_url)]
    img_url = img_url[:len(img_url)-3]
    link = 'http://books.toscrape.com/'
    img_url = link + img_url
    
    
    # image
    #image_url = book.a.img["src"]
    #image_url = urljoin(url, image_url)
    '''
    rows.append([elt, tds[0].text, titre.text, price_ttc, price_ht, tds[5].text, prod_description, category, reviewRating, img_url])
    

        
with open('dataBookCat.csv', 'a') as outfile:
    for url in rows:
        outfile.write((str(url)) + '\n')



