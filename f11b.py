from f11 import list

for i in range(len(list)):
    print(f"{i+1} {list[i]}",end=" ")
    if list[i] > 0:
        print("+")
    else:
        print("-")

