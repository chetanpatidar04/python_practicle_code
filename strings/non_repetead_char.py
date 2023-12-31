# wtp to find first non repeated char in string
def check_non_repeated_char(s):
    # temp = list(s)
    # li = []
    # for i in temp:
    #     if temp.count(i) == 1:
    #         return i
    # return "no char found"
    temp = ""
    for i in range(len(s)):  
        count = 1
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                count += 1
        if count > 1:
            temp = temp + s[i]
        if count == 1 and s[i] not in temp:
            return s[i]
                
        # other possible way is dict
                
           
                
    
    

if __name__ =="__main__":
    s = input("enter the string ")
    print(check_non_repeated_char(s))