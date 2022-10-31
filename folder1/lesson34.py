from bs4 import BeautifulSoup
import urllib.request

# req = urllib.request.urlopen('https://www.sport-express.ru/reviews/')
# html = req.read()
#
# soup = BeautifulSoup(html, 'html.parser')
# news = soup.find_all('div', class_='se-material__content-text se-press-list-page__item-material_right')
# print(news)
# results = []
#
# for item in news:
#     title = item.find('div', class_='se-material__title se-material__title--size-middle se-material__title--bold se-material-list-page__material se-press-list-page__item-material-title').get_text(strip=True)
#     desc = item.find('div', class_='se-material__subtitle').get_text(strip=True)
#     href = item.a.get('href')
#     results.append({
#         'title': title,
#         'desc': desc,
#         'href': href,
#     })
#
#
# f = open('news.txt', 'w', encoding='utf-8')
# i = 1
# for item in results:
#     f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n**********************\n')
#     i += 1
# f.close()

req = urllib.request.urlopen('https://mafiauniverse.org/Players')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
niks0 = soup.find_all('div', class_='w-100')
# niks = soup.find_all('a', class_='fw-bold')
# niks2 = soup.find_all('div', class_='col-2 col-sm-1 px-1')



for item in niks0:
    title = item.find('a', class_='fw-bold')
    # desc = item.find('a', class_='fw-bold').get_text(strip=True)
    # href = item.a.get('href')
    print(title)



# soup = BeautifulSoup(text)
# film_list = soup.find('a', {'class': 'fw-bold'})

# movie_link = item.find('div', {'class': 'fw-bold'}).find('a').get('href')

# mess = f' Tвой рейтинг: <b><u></u></b>'
# bot.send_message(message.chat.id, mess, parse_mode='html'
# print(soup)
# print(niks2)


