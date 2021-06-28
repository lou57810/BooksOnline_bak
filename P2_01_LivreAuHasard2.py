import requests
from bs4 import BeautifulSoup
import csv

# Création d'un dictionnaire et d'une liste de dictionnaires
dataBook = {}
dict_arr = [dataBook]

# Choix d'un livre au hasard
url = 'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'

urlPage = requests.get(url)
soup = BeautifulSoup(urlPage.text, 'html.parser')

# Récupération des valeurs par clé
dataBook['product_page_url'] = url
tdiv = soup.find('table', class_='table table-striped')
tds = tdiv.find_all('td')
    
upc = tds[0].text
dataBook['universal_product_code'] = upc    
    
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
        
numAv = tds[5].text
dataBook['number_available'] = numAv        
    
bal_p = soup.findAll('p')
prod_description = bal_p[3].text
dataBook['prod_description'] = prod_description
    
liste_a = soup.find('ul', class_ = 'breadcrumb').findAll('a')    
category = liste_a[2].text
dataBook['category'] = category
    
reviewRating = tds[6].text
dataBook['review_rating'] = reviewRating    
    
# images    
img_url = soup.find('div',{'id': 'product_gallery'}).find("div", class_='item active').img["src"]    
img_url = img_url[5:]    
link = 'http://books.toscrape.com'
img_url = link + img_url
dataBook['image_url'] = img_url
labels = ['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'prod_description', 'category', 'review_rating', 'image_url']

# Ecriture du fichier csv
try:
    with open('dataBook.csv', 'w', encoding = "utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=labels)
        writer.writeheader()
        for elem in dict_arr:
            writer.writerow(elem)
except IOError:
    print("I/O error")



        




