from bs4 import BeautifulSoup
import urllib.request

class Parserr:

    raw_html = ''
    html = ''
    results = []

    def __init__(self, url, path, elem, elem_class, tit):
        self.url = url
        self.path = path
        self.elem = elem
        self.elem_class = elem_class
        self.tit = tit

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        # self.elem = elem
        # self.elem_class = elem_class


        news = self.html.find_all(self.elem, class_=self.elem_class)

        for item in news:
            title = item.find(self.tit).get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'href': href,
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            i = 1
            for item in self.results:
                f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\n\n**********************\n')
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


# for root, dirs, files in os.walk(path):
#     for file in files:
#         try:
#             path_file = os.path.join(root, file)
#             shutil.move(path_file, path)
#
#         except shutil.Error:
#             continue
#     dir_list.append(root)
#     for root in dir_list[::-1]:
#         if not os.listdir(root):
#             os.rmdir(root)