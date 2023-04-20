temperatura = [0]*7
dienas = ['pirmdiena','otrdiena','trešdiena','ceturtdiena','piektdiena','sestdiena','svētdiena']
for numurs in range(7):
    temperatura[numurs] = int(input('Ievadiet' + dienas[numurs] +'s gaisa temperatūru: '))

dienu_skaits = 0
for numurs in range(7):
    if temperatura[numurs]>25:
        dienu_skaits = dienu_skaits+1

print('Nedēļas karstāko dienu skaits bija ', dienu_skaits)