from random import randint as random

list = [0,0,0,0,0,0,0,0,0,0]

for i in range(len(list)):
    list[i] = int(random(5,25))

print(list)
print(list[::-1])
print(list[1::2])

asd = 0
while True:
    asd = int(input("Ajd meg egy 1-10 közötti számot amit kiir majd a cucc és akkor majd meg fog jelenni a megjelenők listájában, ahol látni fogod a megjelenteket, és láthatatlan lesz a megnemjelentek: "))
    if asd<=10 and asd>=1:
        print(list[asd-1:asd:1])
        break


































































