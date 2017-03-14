import os
PATH = os.getcwd()
lstd = os.listdir('%s/stat_1/stat_gls_mssd_wth_att_1' % PATH)
for folder in lstd:
    if folder[-1] == '~':
        continue
    #os.makedirs('/home/la9ran9e/betting_stat-update/stat_1/stat_gls_mssd_wth_att_1_poss/' + folder)
    lstd_ = os.listdir('%s/stat_1/stat_gls_mssd_wth_att_1/' + folder % PATH)
    for file in lstd_:
        f = open('/home/la9ran9e/betting_stat-update/stat_1/stat_gls_mssd_wth_att_1/' + folder +'/'+ file)
        w_ = open('/home/la9ran9e/betting_stat-update/stat_1/stat_gls_mssd_wth_att_1_poss/' + folder +'/'+ file, 'w')
        home_gls_sum = 0
        away_gls_sum = 0
        for line in f:
            line_ = line.split('\t')
            if line_[0] == 'home':
                home_gls_sum += int(line_[2][:-1])
            elif line_[0] == 'away':
                away_gls_sum += int(line_[2][:-1])
        
            
        f = open('%s/stat_1/stat_gls_mssd_wth_att_1/' + folder +'/'+ file % PATH)
        for line in f:
            line_ = line.split('\t')
            if line_[0] == 'home':
                try:
                    poss = float(int(line_[2][:-1])/home_gls_sum)
                except:
                    poss = 'NA'
            elif line_[0] == 'away':
                try:
                    poss = float(int(line_[2][:-1])/away_gls_sum)
                except:
                    poss = 'NA'
            w = line_[0] +'\t'+ line_[1] +'\t'+ str(poss)
            w_.write(w + '\n')

        
        w_.close()
            
                
            
