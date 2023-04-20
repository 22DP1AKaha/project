temperatura = [0]*7
dienu_skaits = 0
for indekss in range(7):
    temperatura[indekss] = int(input())
    if temperatura[indekss]<-10:
        dienu_skaits = dienu_skaits+1

print(dienu_skaits)