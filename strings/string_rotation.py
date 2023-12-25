# WTP to check is the string is a rotation of other string 
def rotation(str1,str2):
    if len(str1) == len(str2):
        concatenated_str = str1 + str1
        return str2 in concatenated_str
        
    else:
        return False
if __name__ == "__main__":
    string1 = "waterbottle"
    string2 = "erbottlewat"
    print(rotation(string1,string2))