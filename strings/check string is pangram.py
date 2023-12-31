# check if a given string is pangram or not
def is_pangram(str1):
    str1 = str1.replace(" ","")
    li  = list(str1)
    uni = set(li)
    print (li, uni)
    temp = ""
    for i in uni:
        if "a" <= i <="z":
            temp = temp + i
    print(len(temp))
    if len(temp) == 26:
        return True
    else:
        return False
if __name__=="__main__":
    s = input("enter the string ")
    print(is_pangram(s))