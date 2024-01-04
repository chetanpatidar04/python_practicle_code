def fact(a):
    temp = 1
    while(a > 1):
        temp = temp * a
        a -= 1   
    return temp
     

if __name__=="__main__":
    a = int(input("enter  number a "))
    print(fact(a))