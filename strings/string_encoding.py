# encode a string in python (aaaabbbc  -- >4a3b1c)
def encode_str(s):
    # 1st approch
    # temp = ""
    # for i in s:
    #     if i not in temp:
    #         temp = temp + str(s.count(i)) + i
    # return temp
    
    # 2nd approch
    
    temp = ""
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            temp = temp + str(count) + s[i]
            count = 1
    temp = temp + str(count) + s[i]
    return temp
        
        
        
    
        
        

if __name__ =="__main__":
    s = input("enter the string")
    print(encode_str(s))