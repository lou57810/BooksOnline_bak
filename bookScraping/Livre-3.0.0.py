import requests
from bs4 import BeautifulSoup
import csv
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
        
        #print(url)
        appendListe(url, listeUrlLivres)
        i += 1
'''    
    for elt in listeUrlLivres:
         print(elt)
for elt in listeUrlLivres:        
    with open('Livres.txt', 'a') as outfile:
        outfile.write((elt) + '\n')
'''
dataBook = {}
rows = []
labels = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'prod_description', 'category', 'review_rating', 'image_url']

try:    
    with open('dataBookFull.csv', 'w') as f:
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
    #print(url)
    
    #dataBook['product_page_url'] = url
    tdiv = soup.find('table', class_='table table-striped')
    tds = tdiv.find_all('td')
    
    upc = tds[0].text
    #dataBook['universal_product_code'] = upc    
    
    titre = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
    #dataBook['title'] = titre.text    
        
    price_ttc = tds[3].text
    price_ttc = price_ttc[1:len(price_ttc)]
    #dataBook['price_including_tax'] = price_ttc
    
    price_ht = tds[2].text
    price_ht = price_ht[1:len(price_ht)]
    #dataBook['price_excluding_tax'] = price_ht    
        
    numAv = tds[5].text
    #dataBook['number_available'] = numAv        
    
    bal_p = soup.findAll('p')
    prod_description = bal_p[3].text
    #dataBook['prod_description'] = prod_description
        
    liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
    category = liste_a[2].text
    #dataBook['category'] = category
    
    reviewRating = tds[6].text
    #dataBook['review_rating'] = reviewRating    
        
    img_url = soup.find('div',{'id': 'product_gallery'}).find('img')
    img_url = str(img_url)
    img_url = img_url[51:len(img_url)]
    img_url = img_url[:len(img_url)-3]
    link = 'http://books.toscrape.com/'
    img_url = link + img_url
    dataBook['image_url'] = img_url
    
    rows.append([elt, tds[0].text, titre.text, price_ttc, price_ht, tds[5].text, prod_description, category, reviewRating, img_url])
    

        
with open('dataBookFull.csv', 'a') as outfile:
    for url in rows:
        outfile.write((str(url)) + '\n')
        #outfile.write('\n')
 
 

'''    
labels = [['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'prod_description', 'category', 'review_rating', 'image_url']]
df = pd.DataFrame(rows,
                  columns = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'prod_description', 'category', 'review_rating', 'image_url'])
'''

#df = pd.DataFrame(labels)
#df = pd.DataFrame(rows)
#df.to_csv('dataBookFull.csv')

