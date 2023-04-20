masīvs = [0]*1000
elementu_skaits = int(input('ievadi virknes garumu: '))

print('ievadi', elementu_skaits,' skaitļus: ');
print()

for n in range(elementu_skaits):
    masīvs[n] = int(input() )
print()

maz = masīvs[0]
for n in range(1,elementu_skaits):
    if masīvs[n]<maz:
        maz = masīvs[n]

print('Masīva mazākais elements ir: ', maz)