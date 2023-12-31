# check a string is a valid palindrom
def vali_palindrom(s):
    # temp = ""
    # for i in s:
    #     temp = i + temp
    # if temp == s:
    #     return "valid palindrom"
     
    #  2nd approch
    if s[::-1] == s:
        return "valid palindrom string"
    else:
        return "not a valid palindrom string"  
    
    

if __name__ == "__main__":
    s = input("enter a string")
    print(vali_palindrom(s))