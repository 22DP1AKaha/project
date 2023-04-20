dienas = [0]*7

for indekss in range(7):
    dienas[indekss] = int(input())

maz = dienas[0]
maz_indekss = 0

for indekss in range(7):
    if dienas[indekss]<maz:
        maz =  dienas[indekss]
        maz_indekss = indekss

print(maz,maz_indekss+1)