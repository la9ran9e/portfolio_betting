from selenium import webdriver
import time, urllib, os
PATH = os.getcwd()
f = open ('%s/seasons_links' % PATH)
w = open ('%s/matches_links' % PATH, 'w')
browser = webdriver.Chrome('') # path of your chromedriver
try:
    for line in f:
        n = 0
        season_status = ''
        url = line[:-1]
        browser.get(url)
        time.sleep(7)
        while season_status != 'done':
            if n > 0:
        
                prev = browser.find_element_by_id('page_competition_1_block_competition_matches_summary_7_previous')
                prev_html = prev.get_attribute('outerHTML')
                print(prev_html)
                prev_html = prev_html.split('class="')
                print(prev_html)
                prev_class = prev_html[1]
                prev_class = prev_class[:prev_class.index('"')]
                if prev_class == 'previous disabled':
                    season_status = 'done'
                prev.click()
                time.sleep(3)
                try:
                    table_elem = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody')
                except:
                    table_elem = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/table/tbody')
                table_html = table_elem.get_attribute('innerHTML')
                table_html = table_html.split('<tr')
                for i in table_html:
                    if 'class=' in i:
                        if '<td class="score-time score">' not in i:
                            continue
                        i_ = i.split('<td class="score-time score">')
                        match_link = i_[1]
                        match_link = match_link[match_link.index('"')+1:]
                        match_link = match_link[:match_link.index('"')]
                        w.write(match_link + '\n')
                        
                n += 1

            elif n == 0:
                try:
                    table_elem = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody')
                except:
                    table_elem = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/table/tbody')
                table_html = table_elem.get_attribute('innerHTML')
                table_html = table_html.split('<tr')
                for i in table_html:
                    if 'class=' in i:
                        i_ = i.split('<td class="score-time score">')
                        if '<td class="score-time score">' not in i:
                            continue
                        match_link = i_[1]
                        match_link = match_link[match_link.index('"')+1:]
                        match_link = match_link[:match_link.index('"')]
                        w.write(match_link + '\n')
                        
                n += 1
except:
    w.close()
w.close()
