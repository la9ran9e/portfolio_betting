import os
PATH = os.getcwd()
lstd = os.listdir('%s/stat_1/stat_att_1' % PATH)
#os.makedirs('/home/la9ran9e/betting_stat-update/stat_1/stat_att_1_poss')
for file in lstd:
    if file[-1] == '~':
        continue
    w_ = open('%s/stat_1/stat_att_1_poss/'+file % PATH, 'w')
    f = open('%s/stat_1/stat_att_1/'+file % PATH)
    home_att_sum = 0
    away_att_sum = 0
    for line in f:
        line_ = line.split('\t')
        if line_[0] == 'home':
                home_att_sum += int(line_[2][:-1])
        elif line_[0] == 'away':
                away_att_sum += int(line_[2][:-1])
    
    f = open('/stat_1/stat_att_1/'+file % PATH)
    for line in f:
        line_ = line.split('\t')
        if line_[0] == 'home':
            line_ = line.split('\t')
            try:
                poss = float(int(line_[2][:-1])/home_att_sum)
            except:
                poss = 'NA'
        elif line_[0] == 'away':
            try:
                poss = float(int(line_[2][:-1])/away_att_sum)
            except:
                poss = 'NA'
        w = line_[0] +'\t'+ line_[1] +'\t'+ str(poss)
        w_.write(w + '\n')
    w_.close()
