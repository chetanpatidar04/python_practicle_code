
def palindrom(s):
    # if s == s[::-1]:
    #     return ("string is palindrom")
    # else:
    #     return ("string is not palindrom")
    pali = ""
    for i in s:
        pali = i + pali
    if pali == s:
        return "string is palindrom"
    else:
        return "string is not palindrom"
    
        
if __name__ =="__main__":
    s = input(" enter a string ")    
    print(palindrom(s))