list = [0]
poz = 0
valt = 0
for i in range(len(list)):
    if list[i] >= 0:
        poz = 1
    else:
        if poz == 1:
            valt += 1
        poz = 0