#  count words in sentence
def check_words(s):
    # 1st approch
    # li = s.split()
    # return len(li)
    
    # 2nd approch
    li = s.split()    
    count = 0
    for i in li:
        count +=1
    return count               
    
if __name__ =="__main__":
    s = input("enter the string ")
    print(check_words(s))