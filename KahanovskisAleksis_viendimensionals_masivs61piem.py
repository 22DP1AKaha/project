temperatūra = [15,20,26,23,27,25,28]

dienu_skaits = 0
for numurs in range(7):
    if temperatūra[numurs]>25:
        dienu_skaits = dienu_skaits + 1

print('Karstāko dienu skaits bija', dienu_skaits)