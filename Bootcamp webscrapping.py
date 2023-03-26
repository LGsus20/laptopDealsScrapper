from bs4 import BeautifulSoup
import requests

root = 'https://www.reddit.com/r/LaptopDeals/new/?f=flair_name%3A%22%F0%9F%9B%92%24600-%24700%F0%9F%9B%92%22' 
result = requests.get(root)
content = result.text
soup = BeautifulSoup(content, 'lxml')
TITLE = '600-700dlls.text'

box = soup.find_all('article', class_='yn9v_hQEhjlRNZI0xspbA')

links = []
for artic in box:
    for link in artic.find_all('a', href=True):
        if link['href'].startswith("https"):
            links.append(link['href'])

titles = []
for h3 in box:
    for title in h3.find_all('h3', class_='_eYtD2XCVieq6emjKBH3m'):
        titles.append(title.get_text())

my_data = dict(zip(links, titles))

with open(TITLE, 'w') as file:
    for link, title in my_data.items():
        price = title.rsplit("$", 1)[1].split(" ", 1)[0]
        file.write(f"Title: {title}\nPrice: ${price}\nLink: {link}\n\n")