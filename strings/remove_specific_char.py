def remove_char(s,char):
    # s= s.replace("i","")
    temp = ""
    for i in range(len(s)):
        if s[i] == char:
            continue
        temp = temp + s[i]   
    return temp
print(remove_char("this is a string","i"))