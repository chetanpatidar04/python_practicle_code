# handle leading white space 
def remove_spaces(s):
    # 1st approch
    # s.rstrip().lstrip().strip(" ")
    # return s
    
    # 2nd approch
    # temp = "" 
    # for i in s:         
    #     if temp=="" and i == " ":
    #         pass
    #     elif len(temp) > 1  and i==" " and temp[-1] !=" ":
    #         temp = temp + i
    #     elif len(temp) > 1 and i ==" ":
    #         pass
    #     else:
    #         temp = temp + i
    # return temp
    
    # 3rd approch
    return (s.replace("  "," ").replace("  "," "))
    

        

if __name__ == "__main__":
    s = input("enter a string in python")
    print(remove_spaces(s))