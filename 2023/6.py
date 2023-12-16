import math

time = 60808676
distance = 601116315591300
first = 0
last  = 0
numways = 0

for j in range(time):
    if j * (time - j) > distance:
        first = j
        break

for j in range(time):
    if j * (time - j) > distance:
        last = j

numways = (last - first) + 1
print((numways))