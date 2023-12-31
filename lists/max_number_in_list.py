# max number in list
def max_num(li):    
    # 1st approch
    # return max(li)
    
    # 2nd approch
    temp = 0
    for i in li:
        if i > temp:
            temp = i
    return temp        
            
        
    
    
if __name__ == "__main__":
    num = int(input("Enter a number"))
    li = []
    for i in range(num):
        ele = int(input("Enter a number in python"))
        li.append(ele)
    print(max_num(li))
    