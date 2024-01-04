def comman_char(s,s1):
    li=[]
    for i in s:
        if i in s1:
            if i not in li and i != " ":
                li.append(i)
    return li        



print(comman_char("this are some char","2nd string starts from here"))