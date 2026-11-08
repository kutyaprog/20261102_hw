list = ["alma","körte","őszibarack","sárgabarack","szilva","málna","áfonya"]
text = ""
for i in range(len(list)):
    if i != 0:
        text += ","
    text += list[i]