import requests
from bs4 import BeautifulSoup

liste = []

url = 'http://books.toscrape.com/index.html'
response = requests.get(url)

if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')

    
# Catégories:    
    
    match3 = soup.find('ul', class_='nav nav-list')
    match4 = match3.findAll('li')
    
    for li in match4:
        a = li.find('a')
        link = a['href']
        liste.append('http://books.toscrape.com/' + link)

#print(liste)
print(len(liste))

with open('urls.txt', 'w') as file:
    for link in liste:
        file.write(link + '\n')






 
