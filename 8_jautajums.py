from random import randint
masīvs = [0]*1000
elementu_skaits = int(input())
for n in range(elementu_skaits):
    masīvs[n] = randint(10,999)
    print(masīvs[n], end=', ')
print()
paris = 0
neparis = 0
for n in range(elementu_skaits):
    if masīvs[n]%2 == 0:
        paris = paris+1
    if masīvs[n]%2 != 0:
        neparis = neparis+1

print(paris, neparis)
divcipari = 0
triscipari = 0
for n in range(elementu_skaits):
    if masīvs[n]>9 and masīvs[n]<100:
        divcipari = divcipari+1
    if masīvs[n]>99 and masīvs[n]<1000:
        triscipari = triscipari+1
print(divcipari, triscipari)

summa = 0
for n in range(elementu_skaits):
    summa = summa+masīvs[n]
videja_vertiba = summa/elementu_skaits
print(videja_vertiba)

virs = 0
zem = 0
for n in range(elementu_skaits):
    if masīvs[n]>videja_vertiba:
        virs = virs+1
    if masīvs[n]<videja_vertiba:
        zem = zem+1
print(virs, zem)

if zem>virs:
    print('Mazāk ir elementu, kuru vērtība ir virs vidējās vērtības.')
if zem<virs:
    print('Mazāk ir elementu, kuru vērtība ir zem vidējās vērtības.')
