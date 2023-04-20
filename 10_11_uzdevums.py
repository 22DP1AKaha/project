from random import randint

masīvs = [0]*1000
elementu_skaits = int(input())
for n in range(elementu_skaits):
    masīvs[n] = randint(0,100)
    print(masīvs[n], end=', ')
print()
summa = 0
for n in range(elementu_skaits):
    summa = summa+masīvs[n]
videja_vertiba = summa/elementu_skaits
print(videja_vertiba)
lielakais = masīvs[0]
for n in range(elementu_skaits):
    if masīvs[n]>lielakais:
        lielakais = masīvs[n]
print(lielakais)
mazaks_par_pedejo = 0
for n in range(elementu_skaits):
    if masīvs[n]<masīvs[elementu_skaits-1]:
        mazaks_par_pedejo = mazaks_par_pedejo+1
print(mazaks_par_pedejo)
lielaks_par_videjo = 0
for n in range(elementu_skaits):
    if masīvs[n]>(videja_vertiba*2):
        lielaks_par_videjo = lielaks_par_videjo+1
print(lielaks_par_videjo)
