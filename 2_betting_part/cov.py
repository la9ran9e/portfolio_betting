import os
PATH = os.getcwd()
lstd = os.listdir('%s/11th/11th_win_nz' % PATH)
if len(lstd) == 2:
    import cov2
elif len(lstd) == 3:
    import cov3
elif len(lstd) == 4:
    import cov4
