import requests
from bs4 import BeautifulSoup

liste = []

url = 'http://books.toscrape.com/catalogue/category/books/default_15/index.html'

response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    balise_livre = soup.findAll('article', {'class': 'product_pod'})
    #print(len(url_livre))
    #print(url_livre)
    
    for article in balise_livre:
        a = article.find('a')
        link = a['href']
        link = link[8:len(link)]
        liste.append('http://books.toscrape.com/catalogue' + link)
        #print(liste)
        with open('lien.txt', 'w') as file:
            for link in liste:
                file.write(link + '\n')
