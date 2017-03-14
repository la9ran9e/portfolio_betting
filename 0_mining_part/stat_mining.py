import urllib.request as url
import os
PATH = os.getcwd()
f = open('%s/matches_links' % PATH)
wf = open ('%s/src_1' % PATH , 'a')
n = 0
try:
    for link in f:
        n+=1
        print(n)
        if n < 0: # for continue loading to src_1 if it was inerrupted
            continue
        link_ = link.split('/')
        home_team = link_[7]
        away_team = link_[8]
        time = link_[4]+'.'+link_[3]+'.'+link_[2]
        link = 'http://int.soccerway.com' + link[:-1]
        html = url.urlopen(link)
        a = 0
        for i in html:
            i = i.decode('utf-8')
            if 'thick scoretime' in i:
                a = 1
            if a == 3:
                while i[0] == ' ' or i[0] == '\t':
                    i = i[1:]
                score = i[:-1]
                #print(score)
                
                a = 0
            elif a > 0:
                a += 1
            
            if '/charts/statsplus/' in i:
                i_ = i.split("src='")
                src = i_[1]
                src = src[:src.index("'")]
                #print(src)
                w = time +'\t'+ home_team +'\t'+ away_team +'\t'+ score +'\t'+ src
                wf.write(w + '\n')
except:
    wf.close()
wf.close()
            
    
