import requests
from bs4 import BeautifulSoup

liste = []
dico = {}

url = 'http://books.toscrape.com/catalogue/birdsong-a-story-in-pictures_975/index.html'
response = requests.get(url)



if response.ok:
    print("\n")
    dico['product_page_url: '] = url
    print("url:", url)    
    print("\n")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    upc = soup.find('table', {'class': 'table table-striped'}).find('td')
    dico['universal_ product_code (upc): '] = upc.text
    print("UPC:", upc.text)
    
    titre = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
    
    print("Titre:", titre.text)
    
    tds = soup.find('table', {'class': 'table table-striped'}).findAll('td')    
    price_ht = tds[2].text   
    print("Tarif HT: ", price_ht)
    price_ttc = tds[3].text
    print("Tarif TTC: ", price_ttc)
    numAv = tds[5].text
    print("Number available: ", numAv)
    print("\n")    
    
    bal_p = soup.findAll('p')
    prod_description = bal_p[3].text
    print(prod_description)
    print("\n")
    
    liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
    category = liste_a[2].text
    print(category)
    print("\n")
    
    reviewRating = tds[6].text
    print(reviewRating)    
    print("\n")
    
    img_src = soup.find('img')
    print(img_src)
    
    for i in dico.items():
        print(i)
        

   
