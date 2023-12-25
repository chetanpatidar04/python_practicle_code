# WTP to check string contain number or not:
def check_string(s):
    # if s.isdigit():
    #     return True 
    # else:
    #     return False
    li = "0123456789"
    flag = True
    for i in s:
        if i not in li:
            flag = False
            return flag     
    return flag
                    
        

if __name__ == "__main__":
    s = input("Enter the string ")
    print(check_string(s))