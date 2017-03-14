import os
PATH = os.getcwd()
lstd = os.listdir('%s/11th/dump' % PATH)

I = []
I_ = []
E = []
Cov_ = []
for i in lstd:
    J = []
    J_ = []
    for j in lstd:
        f = open('%s/11th/11th_poss' % PATH)
        w = i +','+j
        n = 1
        Ex = 0
        Ey = 0
        for line in f:
            line = line[:-1]
            line_ = line.split('\t')
            if n == 1:
                x = line_.index(i)
                y = line_.index(j)
                portfolio = line[2:]
            else:
                Ex = Ex + float(line_[x])*float(line_[0])
                Ey = Ey + float(line_[y])*float(line_[0])
                    
            n += 1
        if Ex not in E:
            E = E + [Ex]
        f = open('%s/11th/11th_poss' % PATH)
        n = 1
        Cov = 0
        for line in f:
            line = line[:-1]
            line_ = line.split('\t')
            if n == 1:
                x = line_.index(i)
                y = line_.index(j)
            else:
                Cov = Cov + (float(line_[x])- Ex)*(float(line_[y])- Ey)*float(line_[0])
                
            n += 1
        
        J = J + [w]
        J_ = J_ + [Cov]
        Cov_ = Cov_ + [Cov]
    I = I + [J]
    I_ = I_ + [J_]
#print(I_)
#print(E)
#print(Cov_)



import sympy, itertools
def product2(i):
    return i[0]*i[1]


G = []
# изменяется тут
x1 = sympy.Symbol('x1')
x2 = sympy.Symbol('x2')
x3 = sympy.Symbol('x3')
x4 = sympy.Symbol('x4') # до сюда ( можно просто закоментировать)
lmbd = sympy.Symbol('lmbd')

Vars = (x1, x2, x3, x4, lmbd)
#Vars = (x1, x2, x3, lmbd)
#Vars = (x1, x2, lmbd)



    
a = itertools.product((x1, x2, x3, x4), repeat = 2) # еще тут
#a = itertools.product((x1, x2, x3), repeat = 2)
#a = itertools.product((x1, x2), repeat = 2)

V = 0
n = 0
for i in a:
  V = V + Cov_[n]*product2(i)
  n += 1
#print(V)

a = itertools.product((1,-1), repeat = 4) # здесь repeat
#a = itertools.product((1,-1), repeat = 3)
#a = itertools.product((1,-1), repeat = 2)

c = 0
Ws = []
Vs = []
for i in a:
    g = i[0]*x1 +i[1]*x2 + i[2]*x3 + i[3]*x4 - 1 # тут
    #g = i[0]*x1 +i[1]*x2 + i[2]*x3
    #g = i[0]*x1 +i[1]*x2
    G = G + [g]
    c += 1
    print('condition', c, ':', g)
    
    L = V + lmbd * g
    Lds = []
    for i in Vars:
        Ld = sympy.diff(L, i)
        Lds = Lds + [Ld]
    s = sympy.solve(Lds)
    Vx = V.subs([(x1, s[x1]), (x2, s[x2]), (x3, s[x3]), (x4, s[x4])]) # здесь
    #Vx = V.subs([(x1, s[x1]), (x2, s[x2]), (x3, s[x3])])
    #Vx = V.subs([(x1, s[x1]), (x2, s[x2])])
    
    W = ', '.join([str(s[x1]), str(s[x2]), str(s[x3]), str(s[x4])]) # здесь
    #W = ', '.join([str(s[x1]), str(s[x2]), str(s[x3])])
    #W = ', '.join([str(s[x1]), str(s[x2])])
    
    print('W = (',s[x1], s[x2], s[x3], s[x4], ')') # и здесь
    #print('W = (', s[x1], s[x2], s[x3], ')')
    #print('W = (', s[x1], s[x2], ')')
    print('V = ', Vx, '\n')
    Ws = Ws + [W]
    Vs = Vs + [Vx]

Vmin = Vs[0]
Vmin_ = []
for i in Vs:
    if Vmin >= i:
        Vmin = i
c = 0
for i in Vs:
    c += 1
    if Vmin == i:
        Vmin_ = Vmin_ + [c]
print('\n','###########'*5)
print(portfolio)
def scalar(a,b):
    n = 0
    x = 0
    for i in a:
        x += (i*float(b[n]))
    return x
print('\nE =', E, '\n')
for i in Vmin_:
    W = Ws[i-1]
    W = W.split(', ')
    R = scalar(E, W)
    print('\ncondition', i, ':')
    print('W = ', Ws[i-1])
    print('V = ', Vs[i-1])
    print('Revenue =', R)

        
    
