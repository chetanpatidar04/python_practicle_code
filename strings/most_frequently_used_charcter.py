def frequent_char(s):
    di = {}
    for i in s:
        if i == " ":
            continue
        if i not in di.keys():
            di[i] = 1
        else:
            di[i] = di.get(i) + 1
    temp = 0
    temp2 = ""
    for k,v in di.items():
        if temp < v:
            temp,v = v,temp 
            temp2 = k
    return di[temp2],temp2

print(frequent_char("this is a character given as an input"))