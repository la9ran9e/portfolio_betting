import os
PATH_statistics_part = os.getcwd()
os.chdir('../mining_part')
PATH_mining_part = os.getcwd()
lstd = os.listdir('%s/stat_0' % PATH_mining_part)
att = [x for x in range(0,45,4)]
for file in lstd:
    w_ = open ('%s/stat_1/stat_att_1/' + file % PATH_statistics_part, 'w')
    if file[-1] == '~':
        continue

    for x in att:
        c = 0
        if att.index(x) == len(att) - 1:
            break
        f = open ('%s/stat_0/' + file % PATH_mining_part)
        for line in f:
            line_ = line.split('\t')
            if int(line_[4]) >= x and int(line_[4]) < att[att.index(x) + 1] and line_[1] == 'home':
                c += 1
        w = 'home' +'\t'+ str(x) +'-'+str(att[att.index(x) + 1]) +'\t'+ str(c)

        w_.write(w +'\n')
    for x in att:
        c = 0
        if att.index(x) == len(att) - 1:
            break
        f = open ('%s/stat_0/' + file % PATH_mining_part)
        for line in f:
            line_ = line.split('\t')
            if int(line_[4]) >= x and int(line_[4]) < att[att.index(x) + 1] and line_[1] == 'away':
                c += 1
        w = 'away' +'\t'+ str(x) +'-'+str(att[att.index(x) + 1]) +'\t'+ str(c)

        w_.write(w +'\n')
w_.close()
        
        
