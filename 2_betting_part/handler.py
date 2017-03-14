import os
PATH_betting_part = os.getcwd()
os.chdir('../statistics_part')
PATH_mining_part = os.getcwd()
T = {}
T['Bournemouth'] = 'afc-bournemouth'
T['Sunderland'] = 'sunderland-association-football-club'
T['Crystal Palace'] = 'crystal-palace-fc'
T['Burnley'] = 'burnley-fc'
T['Manchester City'] = 'manchester-city-football-club'
T['Middlesbrough'] = 'middlesbrough-football-club'
T['West Ham United'] = 'west-ham-united-fc'
T['Stoke City'] = 'stoke-city-fc'
T['Chelsea'] = 'chelsea-football-club'
T['Everton'] = 'everton-football-club'
T['Arsenal'] = 'arsenal-fc'
T['Tottenham Hotspur'] = 'tottenham-hotspur-football-club'
T['Southampton'] = 'southampton-fc'
T['Hull City'] = 'hull-city-afc'
T['Liverpool'] = 'liverpool-fc'
T['Watford'] = 'watford-football-club'
T['Manchester United'] = 'manchester-united-fc'
T['Swansea City'] = 'swansea-city-afc'
T['Leicester City'] = 'leicester-city-fc'
T['West Brom'] = 'west-bromwich-albion-football-club'
gls1 = [x for x in range(0,11)]
gls2 = [x for x in range(0,11)]

def rem_(path):
    for i in os.listdir(path):
        os.remove(path+'/'+i)


rem_('%s/11th/11th_scores' % PATH_betting_part)
rem_('%s/11th/11th_diff' % PATH_betting_part)
rem_('%s/11th/11th_win' % PATH_betting_part)


f = open ('/11th/11th_odds' % PATH_betting_part)
for match in f:
    match_ = match.split('\t')
    
    m = match_[0]
    m_ = m.split('/')
    
    if m_[1][-3:] == '(h)':
        ht = T[m_[1][:-4]]
        at = T[m_[0]]
        
        sell = str(- float(match_[2][:-1]))
        buy = str(- float(match_[1]))
    else:
        ht = T[m_[0]]
        at = T[m_[1]]
        sell = match_[1]
        buy = match_[2][:-1]
    
    w = '\t'.join([ht, at, sell, buy])        
    print(w)


    lstd = os.listdir('%s/stat_1/stat_gls_mssd_wth_att_1_poss/'+at % PATH_mining_part)
    PP = {}
    for x in gls1:
        for y in gls2:
            poss = []
            #print(x, '-', y)
            t1 = open('%s/stat_1/stat_att_1_poss/'+ht % PATH_mining_part)
            for i in t1:
                i = i.split('\t')
                if i[0] != 'home':
                    continue
                att_poss = i[2][:-1]
                att = i[1]
                #print(att, att_poss)
                for file in lstd:
                    if file[-1] == '~':
                        continue
                    att_ = file[file.index('_') + 1:]
                    if att == att_:
                        t2 = open('%s/stat_1/stat_gls_mssd_wth_att_1_poss/'+at+'/'+file % PATH_mining_part)
                        for j in t2:
                            j = j.split('\t')
                            if j[0] != 'away':
                                continue
                            gls = j[1]
                            gls_poss = j[2][:-1]
                            if gls == str(x):
                                #print(gls, gls_poss)
                                if gls_poss != 'NA':
                                    poss_ = float(att_poss)*float(gls_poss)
                                        
                                else:
                                    poss_ = float(att_poss)*0
                                poss = poss + [str(poss_)]
            P = 0

            for i in poss:
                P += float(i)
            #print(P)
            PP[str(x)+'-'+str(y)] = P


    lstd = os.listdir('%s/stat_1/stat_gls_mssd_wth_att_1_poss/'+ht % PATH_mining_part)
    PP_ = {}
    for x in gls1:
        for y in gls2:
            poss = []
            #print(x, '-', y)
            t1 = open('%s/stat_1/stat_att_1_poss/'+at % PATH_mining_part)
            for i in t1:
                i = i.split('\t')
                if i[0] != 'away':
                    continue
                att_poss = i[2][:-1]
                att = i[1]
                #print(att, att_poss)
                for file in lstd:
                    if file[-1] == '~':
                        continue
                    att_ = file[file.index('_') + 1:]
                    if att == att_:
                        t2 = open('%s/stat_1/stat_gls_mssd_wth_att_1_poss/'+ht+'/'+file % PATH_mining_part)
                        for j in t2:
                            j = j.split('\t')
                            if j[0] != 'home':
                                continue
                            gls = j[1]
                            gls_poss = j[2][:-1]
                            if gls == str(y):
                                #print(gls, gls_poss)
                                if gls_poss != 'NA':
                                    poss_ = float(att_poss)*float(gls_poss)
                                        
                                else:
                                    poss_ = float(att_poss)*0
                                poss = poss + [str(poss_)]
                                        
                    
            P_ = 0

            for i in poss:
                P_ += float(i)
            #print(P_)
            PP_[str(x)+'-'+str(y)] = P_

    P = 0
    d = {}
    try:
        os.makedirs('%s/11th/11th_scores' % PATH_betting_part)
    except:
        None
    f = open('%s/11th/11th_scores/'+ht+'--'+at % PATH_betting_part, 'w')
    for i in PP:
        p = PP.get(i) * PP_.get(i)
        P += p
        #print(i, p)
        d[i] = p
        p = str(p)
        p_ = p.split('.')
        p__ = p_[0]+','+p_[1]
        w = i +'\t'+ p__ +'\t'+ p
        f.write(w+'\n')
    f.close()

    try:
        os.makedirs('%s/11th/11th_diff' % PATH_betting_part)
    except:
        None
    w_ = open('%s/11th/11th_diff/'+ht+'--'+at+'_diff_' % PATH_betting_part, 'w')
    dif = [x for x in range(-10,11)]
    for x in dif:
        P = 0
        f = open('%s/11th/11th_scores/'+ht+'--'+at % PATH_betting_part)
        for line in f:
            line_ = line.split('\t')
            s = line_[0].split('-')
            p = float(line_[2][:-1])
            s1 = int(s[0])
            s2 = int(s[1])
            diff = s1 - s2
            if x == diff:
                P += p
        P = str(P)
        P_ = P.split('.')
        P__ = P_[0] + ',' + P_[1]
        w = str(x) +'\t'+ str(P__) +'\t'+ P
        w_.write(w + '\n')
    w_.close()
    try:
        os.makedirs('%s/11th/11th_win' % PATH_betting_part)
    except:
        None
    
    f = open('%s/11th/11th_diff/'+ht+'--'+at+'_diff_' % PATH)
    w_ = open('%s/11th/11th_win/'+ht+'--'+at+'_win_' % PATH_betting_part, 'w')
    
    for line in f:
        line_ = line.split('\t')
        # замена на (sell+buy)/2
        '''if float(line_[0]) < float(sell):
            win = float(line_[0]) - float(sell)
        elif float(line_[0]) >= float(sell) and float(line_[0]) <= float(buy):
            win = float(0)
        elif float(line_[0]) > float(buy):
            win = float(line_[0]) - float(buy)'''
        # просто закоментирую до... 
        odd_av = (float(sell)+float(buy))/2
        win = float(line_[0]) - odd_av
        # сюда, если что
        w = '\t'.join([str(win), line_[1], line_[2]])
        w_.write(w)
    
    w_.close()
            
        
