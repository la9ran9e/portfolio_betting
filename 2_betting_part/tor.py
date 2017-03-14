from tbselenium.tbdriver import TorBrowserDriver
import time, os
PATH = os.getcwd()
driver = TorBrowserDriver('') # you need a tor browser driver, write path to this
driver.set_page_load_timeout(60)
time.sleep(7)
f = open ('%s/11th/11th_hrefs' % PATH)
n = 0
w_ = open('%s/11th/11th_odds' % PATH, 'w')
def parser(element):
    x = driver.find_element_by_id(element).text
    time.sleep(3)
    #x_h = x_el.get_attribute('outerHTML')
    #x_ = x_h.split('">')
    #x = x_[1]
    #x = x[:x.index('<')]    
    return x

for line in f:
    n += 1
    

    driver.get(line[:-1])
    time.sleep(3)
    
    elem1 = parser('lpRow1')
    elem2 = parser('lpRow2')
    x = elem1+elem2 
    x_ = x.split('\n')
    #print(x_)
    x0 = x_[0]
    
    if x0[0] == ' ':
        x0 = x[1:]
    x1 = x_[1]
    x1_ = x1.split(' ')
    sell = x1_[1]
    buy = x1_[2]
    match = x0

    w = match+'\t'+sell+'\t'+buy
    w_.write(w + '\n')
    
w_.close()
    
driver.close()
    
