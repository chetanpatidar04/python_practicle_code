def swap(a,b):
    temp = a
    a = b
    b = temp
    return "a =" + str(a),"b =" + str(b)

if __name__=="__main__":
    a = int(input("enter  number a"))
    b = int(input("enter  number b"))
    print(swap(a,b))