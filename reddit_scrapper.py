from bs4 import BeautifulSoup
import requests

def webget(root):
    result = requests.get(root)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    box = soup.find_all('article', class_='yn9v_hQEhjlRNZI0xspbA')
    titles = []
    times = []
    links = []
    prices = []
    for i in box:
        time = i.find('span', class_='_2VF2J19pUIMSLJFky-7PEI').get_text()
        if not ("días" in time or "mes" in time):
            times.append(time)
            for title in i.find_all('h3', class_='_eYtD2XCVieq6emjKBH3m'):
                titles.append(title.get_text())
                prices.append(title.get_text().rsplit("$", 1)[1].split(" ", 1)[0])
                
            for link in i.find_all('a', href=True):
                if link['href'].startswith("https"):
                    links.append(link['href'])
    return titles, times, links, prices