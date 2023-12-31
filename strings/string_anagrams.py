def anagrams(s1,s2):
    # if sorted(s1) ==sorted(s2):
    #     return "string are anagrams"
    # else:
    #     return "strings are not anagram"

    if len(s1) == len(s2):
        temp = ""
        for i in s1:
            for j in range(len(s2)):
                if i == s2[j]:
                    temp = temp + i    
        if temp == s1:
            return "true"
    return " not anagram"    
                        
                    
                
    
    
if __name__=="__main__":
    s1 = input("enter the 1st string ")
    s2 = input("enter the 2nd string ")
    print(anagrams(s1,s2))