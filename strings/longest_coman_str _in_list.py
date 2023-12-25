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
                break
            if flag == True and len(li)-1 == j:
                temp = temp + char
                print(temp,len(temp))
    return temp

if __name__ =="__main__":
    check_prefix()
    
    



# def longest_common_prefix(strs):
#     if not strs:
#         return ""
#     first_str, last_str = strs[0], strs[-1]    
#     temp = ""    
#     for i, char in enumerate(first_str):       
#         flag = False
#         for j in range(len(strs)):            
#             if first_str[:len(temp)] != strs[j][:len(temp)]:                
#                 return first_str[:len(temp)-1]
#     # If no difference found, the entire first string is the common prefix
#     return temp

# # Example usage:
# string_list = ['1baa23', 'baaBanana', 'baOrange', 'bapple', 'baplepie', 'banana']
# result = longest_common_prefix(string_list)
# print(result)