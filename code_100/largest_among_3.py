def largest(a,b,c):
    if a > b and a>c: 
        return(str(a) +" a is greater")
    elif b > c:
        return(str(b) +" b is greater")    
    else:
        return(str(c) +" c is greater")    

     

if __name__=="__main__":
    a = int(input("enter  number a "))
    b = int(input("enter  number b "))
    c = int(input("enter  number c "))
    print(largest(a,b,c))