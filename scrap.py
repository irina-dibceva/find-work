import codecs
import time

import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {'User-Agent': 'Mozilla/0.5 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html, application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'http://loveread.ec/index.php?id_genre=14'
url1 = 'http://www.ukrchess.org.ua/'

domain = 'http://loveread.ec/index_book.php?id_genre=14&p='
aa = []
urls = [url]
req = session.get(url, headers=headers)
req1 = session.get(url1, headers=headers)

if req.status_code == 200:
    bsObj = BS(req.content, 'html.parser')
    pagination = bsObj.find('div', attrs={'class': 'navigation'})
    pages = pagination.find_all('a')
    for page in pages:
        p = page.text
        #print(p)
        if p != 'Вперед' :
            urls.append(domain + p)
            print(urls)


for ur in urls:
    time.sleep(2)
    req = session.get(ur, headers=headers)
    if req.status_code == 200:
        bsObj = BS(req.content, 'html.parser')
        table_list = bsObj.find_all('table', attrs={'class': 'table_gl'})
        div_list = bsObj.find_all('div', attrs={'class': 'td_top_text'})
        td_list = bsObj.find_all('td', attrs={'class': 'span_str'})
        for div in table_list:
            title = div.find('strong')
            td = div.find('td', attrs={'class': 'span_str'})
            descr = td.p.text
            aa.append({'title': title, 'descr': descr})




if req.status_code == 200:
    bsObj = BS(req.content, 'html.parser')
    div_list = bsObj.find_all('div', attrs={'class': 'td_top_text'})
    for div in div_list:
        title = div.find('strong')
        #print(title.text)
    td_list = bsObj.find_all('td', attrs={'class':'span_str'})

    #for td in td_list:
        #descr = td.p.text
        #print(descr)
        #href = div.a['href']
        #print(title.text)



template = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"></head><body>'
end = '</body></html>'
content = '<h2> LoveRead</h2>'
for job in aa:
    content += '<a target="_blank">{title}</a><br/><p>{descr}</p><br/>'.format(**job)
    content += '<hr/><br/><br/>'
data = template + content + end
handle = codecs.open('1.html', 'w', 'utf-8')
handle.write(str(data))
handle.close()