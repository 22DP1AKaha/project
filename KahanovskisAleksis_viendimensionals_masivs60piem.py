#programma p60

x = [0]*10

for indekss in range(10):
    x[indekss] = int(input('ievadiet '+str(indekss + 1)+' .skaitli:'))

summa = 0
for indekss in range(10):
    summa = summa + x[indekss] # summas apreiķināšana

print()
print(f'ievadīto skaitļu vidējā vērtība ir {summa/10:0.2f}')
#formatēta izvade ar 2 zīmēm aiz komata