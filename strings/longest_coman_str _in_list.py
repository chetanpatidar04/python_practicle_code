def check_prefix():
    li =  ['baqa23', 'baaBanana', 'baarange', 'baap1ple', 'baaplepie', 'baanana']
    # li.sort()
    if li == []:
        print("")
    temp =""

    # 1st approch
    
    # for i,char in enumerate(li[0]):
        # flag = True    
        # for j in range(1,len(li)):
        #     if li[j][i] != char:
        #         flag = False
        #         continue
        #     print(flag,j,i)
        #     if j == len(li)-1 and flag == True:
        #         temp = temp + char
        
    # 2nd approch
    for i,char in enumerate(li[0]):
        flag = True        
        for j in range(1,len(li)):
            if li[j][:len(temp)] != li[0][:len(temp)]:
                flag = False
                return temp
            else:
                flag = True
                                
        if flag == True:
            temp = temp + char
            flag = False
     
    # If no difference found, the entire first string is the common prefix
    return temp

# Example usage:
string_list = ['baa23', 'baaBanana', 'baOrange', 'bapple', 'baplepie', 'banana']
result = longest_common_prefix(string_list)
print(result)