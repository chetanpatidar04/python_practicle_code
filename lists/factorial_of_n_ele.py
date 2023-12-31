# WTP for factorial of n numbers:
def fact_of_n(n):
    # 1st approch
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_of_n(n-1)
        
    
    # 2nd approch
    # temp = 1
    # for i in li:
    #     temp = temp * i
    # return temp
    
if __name__ =="__main__":
    n = int(input("enter the number"))
    print(fact_of_n(n))