import requests
from bs4 import BeautifulSoup

url = "https://tieba.baidu.com/f?kw=switch&ie=utf-8&tab=main"


def parse_title(soup):
    for a in soup.find_all('a', {'class': 'j_th_tit'}):
        attrs = a.attrs
        title = attrs['title']
        page_id = attrs['href'].split('/')[-1]
        print(page_id, title)


def crawl():
    print('start crawl')
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    parse_title(soup)


if __name__ == '__main__':
    crawl()
