import requests
from bs4 import BeautifulSoup
from lxml.html import etree


headers={"User-agent": 'Mozilla/5.0 (Macintosh; '
                                              'Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, '
                                              'like Gecko) Version/13.0.5 Safari/605.1.15'}
url = "https://movie.douban.com/"


def get_xpath(url):
    try:
        req = requests.request('GET', url, headers=headers)
        html = etree.HTML(req.text)
        return html
    except requests.exceptions.RequestException as error:
        return 'there is a problem : {}'.format(error)


div = get_xpath(url)

hot_topic = div.xpath('//div[@class="billboard-bd"]//td[@class="title"]')
# //td[@class="title"]/a//text()
print(hot_topic)
movies = []
for i in hot_topic:
    print(i.xpath('./a//text()')[0])

