import requests
from bs4 import BeautifulSoup
import csv

liste = []


url = 'http://books.toscrape.com/catalogue/birdsong-a-story-in-pictures_975/index.html'
response = requests.get(url)



if response.ok:
    #dico = {}
    print("\n")
    #dico['product_page_url: '] = url
    print("url:", url)    
    print("\n")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    upc = soup.find('table', {'class': 'table table-striped'}).find('td')
    #dico['universal_ product_code (upc): '] = upc.text
    #print("UPC:", upc.text)
    
    titre = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')
    #dico['title: '] = titre.text
    #print("Titre:", titre.text)
    
    tds = soup.find('table', {'class': 'table table-striped'}).findAll('td')    
    price_ht = tds[2].text 
    #dico['price_excluding_tax: '] = price_ht
    #print("Tarif HT: ", price_ht)
    price_ttc = tds[3].text
    #dico['price_including_tax: '] = price_ttc
    #print("Tarif TTC: ", price_ttc)
    numAv = tds[5].text
    #dico['number_available: '] = numAv
    #print("Number available: ", numAv)
    #print("\n")    
    
    bal_p = soup.findAll('p')
    prod_description = bal_p[3].text
    #dico['product_description: '] = prod_description
    #print(prod_description)
    #print("\n")
    
    liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
    category = liste_a[2].text
    #dico['category: '] = category
    #print(category)
    print("\n")
    
    reviewRating = tds[6].text
    #dico['review_rating: '] = reviewRating
    #print(reviewRating)    
    #print("\n")
    
    img_url = soup.find('img')
    #dico['image_url: '] = img_url
    print(img_url)
    
    #for i in dico.items():
    #    print(i)
        
    #print(dico)
    
    with open('dataPage.csv', mode = 'w') as dataPage:
        csv_file = csv.writer(dataPage, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        csv_file.writerow(['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
        csv_file.writerow([url, upc, titre.text, price_ttc, price_ht, numAv, prod_description, category, reviewRating, img_url])
    
        

   
