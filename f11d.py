from f11 import list

for i in range(1, len(list), 2):
    list[i] -= list[i-1]