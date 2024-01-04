def even_odd(a):
    if a %2 == 0:
        return "even"
    else:
        return "Odd"    

     

if __name__=="__main__":
    a = int(input("enter  number a "))
    print(even_odd(a))