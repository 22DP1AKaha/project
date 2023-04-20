nedelas_dienas = [0]*7
for indekss in range(7):
    nedelas_dienas[indekss] = int(input())

summa = 0
for indekss in range(7):
    summa = summa + nedelas_dienas[indekss]

print(summa/7)