# reverse each word in python
def reverse_words(s):
    # 1st approch
    # li = s.split()
    # for i in range(len(li)):
    #     li[i] = li[i][::-1]
    # return " ".join(li)

    # 2nd approch
    # li = s.split()
    # for i in range(len(li)):
    #     temp = ""
    #     for j in li[i]:
    #         temp = j + temp
    #     li[i] = temp
    # s = " ".join(li)
    
    # 3rd approch
    temp = ""
    temp2 = ""
    for i in s:
        if i !=" ":
            temp = i + temp
        else:
            temp2 = temp2 + " " +temp
            temp = ""
    temp2 = temp2 + " " + temp
    return temp2.strip()
            
    
    return s

    
if __name__=="__main__":
    s = input("Enter the words ")
    print(reverse_words(s))