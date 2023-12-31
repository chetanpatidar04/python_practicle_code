# convert first letter of each word to upper case:
def convert_case(s):
    # 1st approch
    # return s.title()
    
    
    # 2nd approch
    # li = s.split()
    # li2 = [i[0].upper() + i[1:] for i in li]
    # return " ".join(li2)
    
    #3rd approch
    li = s.split()
    li2 =[]
    for i in li:
        li2.append(i.title())
    return " ".join(li2)    
        

if __name__=="__main__":
    s = input("enter the string ")
    print(convert_case(s))
         