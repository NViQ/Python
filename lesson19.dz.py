from bs4 import BeautifulSoup
import urllib.request
import lxml

req = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_utf8.xml')
html = req.read()
print(html)
results = []
Currency = {
    'Valut' : '',
    }

soup = BeautifulSoup(html, features="xml")


for item in soup:
    title = item.find('Name').get_text(strip=True)
    coin = item.find('Value').get_text(strip=True)
    results.append({
        'title': title,
        'coin': coin,

    })

print(results)

# soup = BeautifulSoup(html, 'html.parser')