import requests
from bs4 import BeautifulSoup
import csv

# Adresse de la catégorie (ici catégorie "defaut": 8 pages)
url = 'http://books.toscrape.com/catalogue/category/books/default_15/index.html'

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
    
    for elt in listeUrlLivres:
        print(elt)

