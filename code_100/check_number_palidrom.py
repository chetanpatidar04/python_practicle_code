def palindrom(a):
    temp = a
    rem = 0
    res = 0
    while(a>0):
        rem = a % 10
        a = a // 10
        res = (res * 10) + rem
    if res == temp:
        return "palindrom"
    return "not a palindrom"    


if __name__=="__main__":
    a = int(input("enter number a "))
    print(palindrom(a))