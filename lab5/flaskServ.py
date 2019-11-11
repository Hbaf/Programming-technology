"""
Вход: файл guess.txt содержащий имена для угадывания

(например из http://www.biographyonline.net/people/famous-100.html можно взять имена)


Написать игру "Угадай по фото"

3 уровня сложности:
1) используются имена только 1-10
2) имена 1-50
3) имена 1-100

- из используемых имен случайно выбрать одно
- запустить поиск картинок в Google по выбранному
- получить ~30-50 первых ссылок на найденные по имени изображения
- выбрать случайно картинку и показать ее пользователю для угадывания
  (можно выбрать из выпадающего списка вариантов имен)
- после выбора сказать Правильно или Нет

п.с. сделать серверную часть, т.е. клиент играет в обычном браузере обращаясь к веб-серверу.

п.с. для поиска картинок желательно эмулировать обычный пользовательский запрос к Google
или можно использовать и Google image search API
https://ajax.googleapis.com/ajax/services/search/images? или др. варианты
НО в случае API нужно предусмотреть существующие ограничения по кол-ву запросов
т.е. кешировать информацию на случай исчерпания кол-ва разрешенных (бесплатных)
запросов или другим образом обходить ограничение. Т.е. игра не должна прерываться после N запросов (ограничение API)


п.с. желательно "сбалансировать" параметры поиска (например искать только лица,
использовать только первые 1-30 найденных и т.п.)
для минимизации того что найденная картинка не соответствует имени


"""

import random
import re

from bs4 import BeautifulSoup
from flask import *
import urllib.request

app = Flask(__name__)
url = 'https://www.google.ru/search?tbm=isch&source=hp&q='
names = open('names', 'r').read().split('\n')
pictures = {}

@app.route('/home')
def main_page():
    return render_template('main.html')

@app.route('/rest/<level>')
def get_pic_url(level):
    answer = get_random_name(level)
    # Yeah, i know that send answer to front is not a good idea
    response = {'url': [], 'name_var': [], 'answer': answer}

    if answer not in pictures:
        pictures.update(requets_photos(answer))

    result_names = [answer]
    for i in range(4):
        response['url'].append(get_random_photo(answer))
    i = 0
    while i < 3:
        name = get_random_name(level)
        if name not in result_names:
            result_names.append(name)
            i += 1
    result_names.sort()
    response['name_var'] = result_names
    return jsonify(response)


@app.errorhandler(404)
def not_found():
    redirect(url_for('home'))


def get_random_name(level):
    if level == 'low':
        return names[random.randint(0, 10)]
    if level == 'middle':
        return names[random.randint(0, 50)]
    if level == 'hard':
        return names[random.randint(0, 99)]


def get_random_photo(name):
    return pictures[name][random.randint(0, 10)]

def requets_photos(name):
    loc_url = url + name.replace(' ', '+')
    soup = BeautifulSoup(urllib.request.urlopen(urllib.request.Request(loc_url, headers={'User-Agent': 'Mozilla/5.0'})), 'html.parser')
    result = {name: []}
    result[name].extend([a['src'] for a in soup.find_all("img", {"src": re.compile("(biographyonline.net|(gstatic|bloomberg|biography).com|wikipedia.org)")})])
    return result
