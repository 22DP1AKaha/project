sk=[0,0,0,0,0,0,0,0,0,0]
for indekss in range(10):
    sk[indekss] = int(input('Ievadiet '+str(indekss+1)+'. skaitli: '))
summa = 0
for indekss in range(10):
    summa = summa +sk[indekss]
print(summa)