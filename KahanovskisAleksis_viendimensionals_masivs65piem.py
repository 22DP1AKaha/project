lv = [''] * 7
en = lv.copy()

lv[0] = 'suns'
lv[1] = 'kaķis'
lv[2] = 'cālis'
lv[3] = 'pīle'
lv[4] = 'govs'
lv[5] = 'zirgs'
lv[6] = 'aita'

en[0] = 'dog'
en[1] = 'cat'
en[2] = 'chicken'
en[3] = 'duck'
en[4] = 'cow'
en[5] = 'horse'
en[6] = 'sheep'

vards = input('Ievadi vārdu latviski:')

for i in range(7):
    print(lv[i])
    if vards == lv[i]:
        print(lv[i],'=',en[i])
        #print(en[lv.index(vards)])