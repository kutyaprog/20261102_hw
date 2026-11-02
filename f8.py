list = [0,0,0,0,0,0]

for i in range(len(list)-1):
    print(i)
    if list[i+1] %2 == 0 and i == len(list):
        list[i+1] =+ list[i+2]
    elif i == len(list)-1:
        break

