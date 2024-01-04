def swap(a,b):
    # a,b = b,a  5,4         approch 1
    a = a+b
    b = a-b
    return "a =" + str(a),"b =" + str(b)

if __name__=="__main__":
    a = int(input("enter  number a"))
    b = int(input("enter  number b"))
    print(swap(a,b))