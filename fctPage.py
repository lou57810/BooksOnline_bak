import requests
from bs4 import BeautifulSoup
import csv

liste = []


url = 'http://books.toscrape.com/catalogue/birdsong-a-story-in-pictures_975/index.html'
response = requests.get(url)



if response.ok:
    
    print("\n")
    
    print("url:", url)    
    print("\n")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    upc = soup.find('table', {'class': 'table table-striped'}).find('td')    
    
    titre = soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1')    
    
    tds = soup.find('table', {'class': 'table table-striped'}).findAll('td')    
    price_ht = tds[2].text 
    
    price_ttc = tds[3].text
    
    numAv = tds[5].text
        
    
    bal_p = soup.findAll('p')
    prod_description = bal_p[3].text    
    
    liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
    category = liste_a[2].text
    
    print("\n")
    
    reviewRating = tds[6].text
    
    
    img_url = soup.find('div',{'id': 'product_gallery'}).find('img')
    img_url = str(img_url)
    img_url = img_url[51:len(img_url)]
    img_url = img_url[:len(img_url)-3]
    link = 'http://books.toscrape.com/'
    img_url = link + img_url
    
    
    print(img_url)    
    
    with open('dataPage.csv', mode = 'w') as dataPage:
        csv_file = csv.writer(dataPage, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
        csv_file.writerow(['product_page_url', 'universal_product_code(upc)', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
        csv_file.writerow([url, upc, titre.text, price_ttc, price_ht, numAv, prod_description, category, reviewRating, img_url])
    
        

   
