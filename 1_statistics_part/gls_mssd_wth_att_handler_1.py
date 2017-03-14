import os
PATH_statistics_part = os.getcwd()
os.chdir('../mining_part')
PATH_mining_part = os.getcwd()
lstd = os.listdir('%s/stat_0' % PATH_mining_part)
att = [x for x in range(0,45,4)]
gls = [str(x) for x in range(11)]
for file in lstd:
    if file[-1] == '~':
        continue
    #os.makedirs('/home/la9ran9e/betting_stat-update/stat_1/stat_gls_mssd_wth_att_1/' + file)

for file in lstd:
    if file[-1] == '~':
        continue
    for x in att:
        if att.index(x) == len(att) - 1:
            break
        w_ = open ('%s/stat_1/stat_gls_mssd_wth_att_1/'+ file +'/'+ file +'_'+str(x)+'-'+str(att[att.index(x) + 1]) % PATH_statistics_part, 'w')
    #home (gls|att)
        for y in gls:
            c = 0
            f = open('%s/stat_0/'+file % PATH_mining_part)
            for i in f:
                i_ = i.split('\t')
                if i_[1] == 'home' and  int(i_[5][:-1]) >= x and int(i_[5][:-1]) < att[att.index(x) + 1]  and y == i_[2]:
                    c += 1
                    
            w = 'home' +'\t'+ y +'\t'+ str(c)
            w_.write(w +'\n')
 #away (gls|att)
        for y in gls:
            c = 0
            f = open('%s/stat_0/'+file % PATH_mining_part)
            for i in f:
                i_ = i.split('\t')
                if i_[1] == 'away' and  int(i_[5][:-1]) >= x and int(i_[5][:-1]) < att[att.index(x) + 1]  and y == i_[2]:
                    c += 1
                    
            w = 'away' +'\t'+ y +'\t'+ str(c)
            w_.write(w +'\n')

        w_.close()
        
