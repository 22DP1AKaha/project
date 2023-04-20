n_kvadrata = [0]*100
n_kuba = [0]*100
aritmetiska_prog_3 = [0]*101
aritmetiska_prog_10 = [0]*101
aritmetiska_prog_2 = [0]*101

aritmetiska_prog_3[0] = 3
aritmetiska_prog_10[0] = 10
aritmetiska_prog_2[0] = 2
for indekss in range(1,100):
    n_kvadrata[indekss-1] = indekss*indekss
    n_kuba[indekss-1] = indekss*indekss*indekss
    aritmetiska_prog_3[indekss] = aritmetiska_prog_3[indekss-1]+3
    aritmetiska_prog_10[indekss] = aritmetiska_prog_10[indekss-1]-2
    aritmetiska_prog_2[indekss] = aritmetiska_prog_2[indekss-1]*2 

reizes = int(input())
for indekss in range(reizes):
    print(n_kvadrata[indekss], end=', ')
print()
for indekss in range(reizes):
    print(n_kuba[indekss], end=', ')
print()
for indekss in range(reizes):
    print(aritmetiska_prog_3[indekss], end=', ')
print()
for indekss in range(reizes):
    print(aritmetiska_prog_10[indekss], end=', ')
print()
for indekss in range(reizes):
    print(aritmetiska_prog_2[indekss], end=', ')
