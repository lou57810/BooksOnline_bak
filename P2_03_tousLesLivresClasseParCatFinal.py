import requests
from bs4 import BeautifulSoup
import csv
import urllib.request
from urllib.parse import urljoin
from csv import DictWriter
import time
import shutil 
import os   # for creation 'img' & listeParCat directory


dataBook = {}
dict_arr = [dataBook]
listeUrlImg = []

try:
   os.mkdir('img')
except:
    print('fail to create img directory')
print('img created')

try:
   os.mkdir('listeParCat')
except:
    print('fail to create listeParCat directory')
print('listeParCat created')



# Fonction -------------------------------------------------------------------------------
def imgDownload(URL):
    image = URL.rsplit('/', 1)[1]    
    urllib.request.urlretrieve(URL, 'img/' + image)
    #sleep(1)
# End -----------------------------------------------------------------------------------

# Fonction -------------------------------------------------------------------------------
def dataLivre(url, dataBook):    
    urlPage = requests.get(url)
    soup = BeautifulSoup(urlPage.text, 'html.parser')
    # url
    dataBook['product_page_url'] = url
    # -----------------------------------------------------
    tdiv = soup.find('table', class_='table table-striped')
    tds = tdiv.find_all('td')
    # universal_product_code ------------------------------   
    upc = tds[0].text
    dataBook['universal_product_code'] = upc
    # titre
    titre = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
    dataBook['title'] = titre.text    
    # price_ttc
    price_ttc = tds[3].text
    price_ttc = price_ttc[1:len(price_ttc)]
    dataBook['price_including_tax'] = price_ttc
    # price_ht
    price_ht = tds[2].text
    price_ht = price_ht[1:len(price_ht)]
    dataBook['price_excluding_tax'] = price_ht
    # numAv
    numAv = tds[5].text
    dataBook['number_available'] = numAv
    # prod_description
    bal_p = soup.findAll('p')
    prod_description = bal_p[3].text
    dataBook['prod_description'] = prod_description
    # catégorie
    liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
    category = liste_a[2].text
    dataBook['category'] = category
    # review_rating
    reviewRating = tds[6].text
    dataBook['review_rating'] = reviewRating                       
       
    # images    
    img_url = soup.find('div',{'id': 'product_gallery'}).find("div", class_='item active').img["src"]    
    img_url = img_url[5:]    
    link = 'http://books.toscrape.com'
    img_url = link + img_url    
    
    dataBook['image_url'] = img_url
    
# End ---------------------------------------------------------------------------------

# Adresses des catégories -------------------------------------------------------------
listeCategory = []
urlIndex = 'http://books.toscrape.com/index.html'
response = requests.get(urlIndex)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    match3 = soup.find('ul', class_='nav nav-list')           
    
    tdi = match3.findAll('li')
    i = 1
    # 50 livres - pageRéf(book)
    while i < 51:
        a = tdi[i].find('a')
        link = a['href']
        listeCategory.append('http://books.toscrape.com/' + link)        
        i+=1

# ---------------------------------------------------------------------------------------

def listeLivresParCat(url, listeUrlLivres):
     # Liste des adresses livres par pages de la categorie 
    urlPage = requests.get(url)
    if urlPage.ok:
        soup = BeautifulSoup(urlPage.text, 'html.parser')
            
    balise_livre = soup.findAll('article', {'class': 'product_pod'})        
    for article in balise_livre:
        a = article.find('a')
        link = a['href']
        link = link[8:len(link)]
        listeUrlLivres.append('http://books.toscrape.com/catalogue' + link)
        
# End ---------------------------------------------------------------------------------

# main --------------------------------------------------------------------------------

k = 1

for urlCategory in listeCategory:
    #print(urlCategory)    
    radical = 'listeParCat/livresCat'
    ext = '.csv'
    titre = radical + str(k) + ext
    
    #print(titre)
    labels = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'prod_description', 'category', 'review_rating', 'image_url']
    
    try:
        with open(titre, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writeheader()                                
    except IOError:
        print("I/O error")
    
    listeUrlLivres = []
    
    urlPage = requests.get(urlCategory)
    if urlPage.ok:        
        soup = BeautifulSoup(urlPage.text, 'html.parser')
    
    # Récupération du nombre de livres
    nbrLivres = (soup.find('form').find('strong')).text
    nbrLivres = int(nbrLivres)    
        
    nbrPage = 0    
    if ((nbrLivres%20)>0):
        nbrPage = int((nbrLivres/20)+1)
        
                        
    if (nbrPage == 1):
        listeLivresParCat(urlCategory, listeUrlLivres)
                        
    else:        
        listeLivresParCat(urlCategory, listeUrlLivres)        
        url_base = urlCategory[0:(len(urlCategory) -10)]        
                    
        i = 2
        while i <= nbrPage:
            linkPage = 'page-' + str(i) + '.html'
            url = url_base + linkPage
                        
                                                                            
            listeLivresParCat(url, listeUrlLivres)                          # append la totalité des livres de chaque page de la catégorie            
            i += 1
            
            
         
          
    for elt in listeUrlLivres:        
        dataLivre(elt, dataBook) 
        URL = (dataBook['image_url'])
        imgDownload(URL)
        dict_arr = [dataBook]
        try:
            with open(titre, 'a', encoding='utf-8') as f:           
                for elem in dict_arr:                    
                    writer = csv.DictWriter(f, fieldnames=labels)
                    writer.writerow(elem)
        except IOError:
            print("I/O error")    
    k += 1

# -------------------------------------------------------------------------------------
     
        

        

        
