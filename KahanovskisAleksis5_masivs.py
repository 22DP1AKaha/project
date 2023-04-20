skaitlis = [0]*30
skaitlis[0] = 1
skaitlis[1] = 1
for indekss in range(2,30):
    skaitlis[indekss] = skaitlis[indekss-2]+skaitlis[indekss-1]
for indekss in range(30):
    print(skaitlis[indekss], end=', ')