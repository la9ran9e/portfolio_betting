import urllib.request as url
import os
PATH = os.getcwd()


def check_file(file_name):
    try:
        file = open('%s/stat_0/' + file_name % PATH)
        file.close()
    except:
        file = open('%s/stat_0/' + file_name % PATH, 'w')
        file.close()

        
f = open ('%s/src_1' % PATH)
n = 0
for line in f:
    n+=1
    print(n)
    if n < 0: # for continue loading to src_1 if it was inerrupted
        continue
    if len(line) < 5:
        continue
    line_ = line.split('\t')
    time = line_[0]
    home_team = line_[1]
    away_team = line_[2]
    score = line_[3]
    link = 'http://int.soccerway.com'+line_[4][:-1]
    home_team_scored = score[0]
    home_team_missed = score[4]
    away_team_scored = home_team_missed
    away_team_missed = home_team_scored
    
    html = url.urlopen(link)
    a = 0
    b = 0
    for i in html:
        i = i.decode('utf-8')
        if 'legend left value' in i:
            a += 1
            if a == 2:
                home_done_on_target = i[i.index('>') + 1:]
                home_done_on_target = home_done_on_target[:home_done_on_target.index('<')]
                #print(home_done_on_target)
            if a == 3:
                home_done_wide = i[i.index('>') + 1:]
                home_done_wide = home_done_wide[:home_done_wide.index('<')]
                #print(home_done_wide)
                home_att_done = str(int(home_done_on_target) + int(home_done_wide))
                #print(home_att_done)
                away_att_seen = home_att_done

        if 'legend right value' in i:
            b += 1
            if b == 2:
                away_done_on_target = i[i.index('>') + 1:]
                away_done_on_target = away_done_on_target[:away_done_on_target.index('<')]
                #print(home_done_on_target)
            if b == 3:
                away_done_wide = i[i.index('>') + 1:]
                away_done_wide = away_done_wide[:away_done_wide.index('<')]
                #print(home_done_wide)
                away_att_done = str(int(away_done_on_target) + int(away_done_wide))
                #print(away_att_done)
                home_att_seen = away_att_done

        if a == 3 and b == 3:
            check_file(home_team)
            check_file(away_team)
            f1 = open('%s/stat_0/' + home_team % PATH, 'a')
            f2 = open('%s/stat_0/' + away_team % PATH, 'a')
            hw = time +'\t'+ 'home' +'\t'+ home_team_scored +'\t'+ home_team_missed +'\t'+ home_att_done +'\t'+ home_att_seen
            f1.write(hw+'\n')
            f1.close()
            aw = time +'\t'+ 'away' +'\t'+ away_team_scored +'\t'+ away_team_missed +'\t'+ away_att_done +'\t'+ away_att_seen
            f2.write(aw+'\n')
            f2.close()
            break
            
 

            
                
            
    
    
