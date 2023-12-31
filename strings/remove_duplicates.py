#  wTP remove duplicates from the string
def remove_string(s):
    temp = ""
    for i in range(len(s)):
        if s[i] not in s[i+1:]:    
            temp = temp + s[i]
    return temp
    
if __name__ == "__main__":
    str1 = input("enter the string")
    print(remove_string(str1))