sk = [0]*10
for indekss in range(10):
    sk[indekss] = int(input())

maz = sk[0]
for indekss in range(10):
    if sk[indekss]>maz:
        maz = sk[indekss]
print(maz)