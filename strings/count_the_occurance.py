#  count the occurance of sub string in python

def count_substring(string,sub):
    temp = ""
    count = 0
    return string.count(sub)
        
    # for i in range(len_main - len_sub + 1):
    #     # Check if substring matches at the current position
    #     if main_string[i:i + len_sub] == substring:
    #         count += 1
                            
        
    
    
if __name__=="__main__":
    string = input("enter the string")
    sub = input("enter the sub string to be find ")
    print(count_substring(string,sub))
    