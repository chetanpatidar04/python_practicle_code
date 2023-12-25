# WTP to check given ipv6 address is valid or not
import re
def validate_ip(s):
    #1st approch
    # ads = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')
    # return bool(ads.match(s))

    # 2nd approch
    li= s.split(":")
    al = ["a","b","c","d","e","f","A","B","C","D","E","F"]    
    if len(li) == 8:
        for i in li:
            if i.isdigit():
                continue            
            for j in range(len(i)):
                if not i[j].isdigit() and not i[j] in al:
                    return False
    else:
        return False    
    return True
        
if __name__ =="__main__":
    s = input("enter a ip address ")
    print(validate_ip(s))