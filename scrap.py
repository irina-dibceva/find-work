import codecs

import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {'User-Agent': 'Mozilla/0.5 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'http://loveread.ec/index.php?id_genre=14'
url1 = 'http://www.ukrchess.org.ua/'

domain = 'http://loveread.ec'
aa = []
urls = [url]
req = session.get(url, headers=headers)
req1 = session.get(url1, headers=headers)

if req.status_code == 200:
    bsObj = BS(req.content, 'html.parser')
    div_list = bsObj.find_all('div', attrs={'class': 'td_top_text'})
    #print(div_list.text)
    for div in div_list:
        title = div.find('strong')
        #href = div.a['href']
        print(title.text)

if req1.status_code == 200:
    bsObj = BS(req1.content, 'html.parser')
    div_list = bsObj.find_all('div', attrs={'class': 'anons'})
    #print(div_list.text)
    for div in div_list:
        title = div.find('span')
        #href = div.a['href']
        print(title.text)

#data = bsObj.prettify()#.encode('utf8')

   # handle = codecs.open('1.html', 'w', 'utf-8')
    #handle.write(str(div_list))
 #handle.close()