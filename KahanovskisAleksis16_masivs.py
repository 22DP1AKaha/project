masivs = [0]*1000
n = int(input())

for indekss in range(n):
    masivs[indekss] = int(input())
for indekss in range(n):
    print(masivs[indekss], end=', ')\

print()
pozitivi_sk = 0
negativi_sk = 0
for indekss in range(n):
    if masivs[indekss]>0:
        pozitivi_sk = pozitivi_sk+1
    elif masivs[indekss]<0:
        negativi_sk = negativi_sk+1

if negativi_sk == 0 and pozitivi_sk>0:
    print('Nav negatīvu elementu.')
elif pozitivi_sk == 0 and negativi_sk>0:
    print('Nav pozitīvu elementu.')
elif pozitivi_sk>negativi_sk:
    print('Vairāk ir pozitīvu elementu.') 
elif pozitivi_sk<negativi_sk:
    print('Vairāk ir negatīvu elementu.')
elif pozitivi_sk==negativi_sk and pozitivi_sk+negativi_sk!=0:
    print('Pozitīvu un negatīvu elementu skaits ir vienāds.')
elif negativi_sk == 0 and pozitivi_sk == 0:
    print('Visi elementi ir 0, jeb nav pozitīvu un negatīvu elementu.')

divciparu_sk = 0
trisciparu_sk = 0
for indekss in range(n):
    if masivs[indekss]>9 and masivs[indekss]<100:
        divciparu_sk = divciparu_sk+1
    elif masivs[indekss]<-9 and masivs[indekss]>-100:
        divciparu_sk = divciparu_sk+1
    elif masivs[indekss]>99 and masivs[indekss]<1000:
        trisciparu_sk = trisciparu_sk+1
    elif masivs[indekss]<-99 and masivs[indekss]>-1000:
        trisciparu_sk = trisciparu_sk+1

if trisciparu_sk == 0 and divciparu_sk>0:
    print('Nav trīsciparu elementu.')
elif divciparu_sk == 0 and trisciparu_sk>0:
    print('Nav divciparu elementu.')
elif divciparu_sk>trisciparu_sk and trisciparu_sk!=0:
    print('Vairāk ir elementi, kuri ir divciparu skaitļi.')
elif trisciparu_sk>divciparu_sk and divciparu_sk!=0:
    print('Vairāk ir elementi, kuri ir trīsciparu skaitļi.')
elif divciparu_sk==0 and trisciparu_sk == 0:
    print('Nav divciparu vai trīsciparu elementu.')

lielaks = 0
mazaks = 0
for indekss in range(n-1): 
    if masivs[indekss]>masivs[n-1]:
        lielaks = lielaks+1
    if masivs[indekss]<masivs[n-1]:
        mazaks = mazaks+1

if lielaks == 0 and mazaks == 0:
    print('Nav lielāku vai mazāku elementu.')
elif lielaks == 0 and mazaks>0:
    print('Nav lielāku elementu par pēdējo masīva elementu.')
elif mazaks>lielaks and lielaks>0:
    print('Vairāk ir elementu, kuru vērtība ir mazāka par pēdējo masīva elementu.')
elif lielaks>mazaks and mazaks>0:
    print('Vairāk ir elementu, kuru vērtība ir lielāka par pēdējo masīva elementu.')
elif mazaks == 0 and lielaks>0:
    print('Nav mazāku elementu par pēdējo masīva elementu.')