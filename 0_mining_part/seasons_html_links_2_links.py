import os
PATH = os.getcwd()
f = open ('%s/seasons_html_links' % PATH)
w = open ('%s/seasons_links' % PATH, 'w')
f = f.read()
f = f.split('value')
for i in f:
    if i[0] != '=':
        continue
    else:
        link = i[i.index('=') + 2:]
        link = link[:link.index('"')]
        link = 'http://int.soccerway.com' + link
        w.write(link + '\n')
w.close()
        
        
