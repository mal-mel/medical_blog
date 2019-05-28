from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

import requests
import bs4
import re
import time


def parser(news_object):
    html_links = requests.get('http://neuronews.ru/index.php/novosti/').text
    soup_links = bs4.BeautifulSoup(html_links, 'html.parser')

    links = []

    for link in soup_links.find_all('h3', class_='catItemTitle'):
        links.append(re.findall('href="(.+)"', str(link.find('a'))))

    for link in links:

        try:
            if f'http://neuronews.ru{link[0]}' == news_object.objects.get(source=f'http://neuronews.ru{link[0]}').source:
                continue
        except ObjectDoesNotExist:

            text = ''
            html_article = requests.get(f'http://neuronews.ru{link[0]}').text

            soup_article = bs4.BeautifulSoup(html_article, 'html.parser')
            title = soup_article.find(id='k2Container').find(class_='itemTitle').text.strip()

            title = title.replace('/', '\\')

            for tag in soup_article.find(id='k2Container').find_all('p'):
                text += tag.text + '\n\n'

            string = re.findall(r'Текст: .+', text)[0] if re.findall(r'Текст: .+', text) else ''

            text = text.replace(string, '')
            text = text.replace('Источник', '')
            text += f'Источник: http://neuronews.ru{link[0]}'

            try:
                news_object.objects.get(title=title)
            except ObjectDoesNotExist:
                news_object.objects.create(title=title, content=text, source=f'http://neuronews.ru{link[0]}', slug=slugify(title, allow_unicode=True) + '-' + str(int(time.time())))

    return news_object
