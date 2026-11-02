import random

list = [0,0,0,0,0,0,0]
for i in range(len(list)):
    list[i] = bool(random.randint(0,1))

for i in range(len(list)):
    if list[i] == 1:
        print("Igaz")
    else:
        print("Hamis")