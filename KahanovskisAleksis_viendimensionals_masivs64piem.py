from random import randint
x = [0]*100

elementu_skaits = int(input('ievadi masīva elementu skaitu:'))

#1
for k in range(elementu_skaits):
    x[k] = randint(1,1000)

for k in range(elementu_skaits):
    print(f'{x[k]:4d}',end='')
print()
#2
z = 0
for k in range(elementu_skaits):
    if x[k]%2==1:
        z = z+1
print('Nepāra skaitļi ir ',z)
input('nospiež ENTER taustiņu')

#3
maz = x[0]
for k in range(1,elementu_skaits):
    if x[k]< maz:
        maz =[k]
print('Masīva mazākais elements ir: ', maz)
input('nospiež ENTER taustiņu')

#4
sum = 0
for k in range(elementu_skaits):
    sum = sum+x[k]

print(f'Masīva elementu vidējā aritmētiskā vērtība ir {sum/elementu_skaits:0.2f}')