import os
PATH = os.getcwd()
lstd = os.listdir('%s/11th/dump' % PATH)
for i in lstd:
    os.remove('%s/11th/dump/'+i % PATH)
    
lstd = os.listdir('%s/11th/11th_win_nz' % PATH)
N = 1
for file in lstd:
    if file[-1] == '~':
        continue
    f = open('%s/11th/11th_win_nz/'+file % PATH)
    n = 0
    for i in f:
        n += 1
    N = N*n
print('\nNumber of results:', N)
NN = N

last_file = file
a = 0
w_ = open('%s/11th/dump/'+last_file[:last_file.index('_')] % PATH, 'w')
f = open('%s/11th/11th_win_nz/'+last_file % PATH)
n = 0
for i in f:
    n += 1
N = N/n
N_ = 0
while N_ < N:
    f = open('%s/11th/11th_win_nz/'+last_file % PATH)
    for i in f:
        i_ = i.split('\t')
        win = i_[0]
        poss = i_[2][:-1]
        w = win+'\t'+poss
        w_.write(w +'\n')
        a += 1
        
        
    N_ += 1
w_.close()
n_ = n
for file in lstd:
    if file == last_file:
        continue
    f = open('%s/11th/11th_win_nz/'+file % PATH)
    w_ = open('%s/11th/dump/'+file[:file.index('_')] % PATH, 'w')
    n = 0
    for i in f:
        n += 1
    N = N/n
    N_ = 0
    
    while N_ < N:
        f = open('%s/11th/11th_win_nz/'+file % PATH)
        m = 0
        for i in f:
            i_ = i.split('\t')
            win = i_[0]
            poss = i_[2][:-1]
            w = win+'\t'+poss
            N__ = 0
            while N__ < n_:
                w_.write(w +'\n')
                N__ += 1
                m += 1
        N_ += 1
    w_.close()
    n_ = m            
            
        
lstd = os.listdir('%s/11th/dump' % PATH)

l = [[1]]
while len(l) < NN:
    l = l + [['1']]
#print(l)
w_ = open('%s/11th/11th_poss' % PATH,'w')
w = 'p'+'\t'+ '\t'.join(lstd)
w_.write(w+'\n')
for file in lstd:
    c = 0
    f = open('%s/11th/dump/'+file % PATH)
    for i in f:
        poss = i.split('\t')[1][:-1]
        win = i.split('\t')[0]
        #print(l[c])
        #print(l[c][0])
        l[c][0] = str(float(l[c][0])*float(poss))
        l[c] = l[c] + [win]
        #print(l[c])
        c += 1
c = 0
for i in l:
    c += 1
    w = '\t'.join(i)
    w_.write(w+'\n')
w_.close()
        
    
    
