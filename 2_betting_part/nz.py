import os
PATH = os.getcwd()
lstd = os.listdir('%s/11th/11th_win' % PATH)
lstd_ = []
for i in lstd:
    lstd_ += [i[:-5]]
n = 1

for i in lstd_:
    print('\n', n, i)
    n += 1
choice = input('\n\tChoose matches [min 2, max 4]: ')
choice = choice.split(' ')
choice.sort()
lstd1 = []
for i in choice:
    lstd1 += [lstd[int(i)-1]]
a = os.listdir('%s/11th/11th_win_nz' % PATH)
for i in a:
    os.remove('%s/11th/11th_win_nz/'+i % PATH)


    
for file in lstd1:
    w_ = open('%s/11th/11th_win_nz/'+file+'nz' % PATH, 'w')
    f = open('%s/11th/11th_win/'+file % PATH)
    for i in f:
        i_ = i.split('\t')
        poss = float(i_[2][:-1])
        if poss == 0:
            continue
        else:
            w_.write(i)
    w_.close()

