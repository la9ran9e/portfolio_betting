import socks, socket, requests, os
from bs4 import BeautifulSoup
PATH = os.getcwd()
socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr = "127.0.0.1", port = 9050)
socket.socket = socks.socksocket
html_doc = requests.get("http://www.sportingindex.com/spread-betting/football/domestic-premier-league").text
n = 0
hrefs = []
w_ = open ('%s/11th/11th_hrefs' % PATH, 'w')
soup = BeautifulSoup(html_doc, 'html.parser')
Elems = soup.find_all("tr")
for el in Elems:
    
    t = el.find("td", class_ = 'time')
    
    if t:
        elem = el.find("td", class_ = 'meeting')
        #print(elem)
        href_ = elem.find('a')
        #print(href_)
        try:
            href = href_.get('href')
        except:
            continue
        
        # внимание! костыль!
        #из-за того, что bs4 каким-то неведомым образом дублирует строки исходника,
        #придется сохранять ссылки в лист h
        #и сравнивать перед сохранением в документ
        if href not in hrefs:
            w = 'http://www.sportingindex.com' + href
            w_.write(w +'\n')
            hrefs = hrefs + [href]
        
            n += 1
print('Number of matches:', n)
w_.close()
