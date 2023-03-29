# programma p59
from random import randint

A = [0] * 10

for indekss in range(10):
    A[indekss] = randint(1,15)

print('Masīvs A:')
for indekss in range(10):
    print(A[indekss], end = '\t')
print()
print()
print('iegūto skaitļu virkne:')
for indekss in range(8):
    print(A[indekss] + A[indekss+1] + A[indekss+2], end = '\t')