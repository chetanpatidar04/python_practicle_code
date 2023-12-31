def fact_num(n):
    factors = []
    temp = n 
    while(n > 0):        
        print(n)
        if temp % n == 0 :
            factors.append(n)
        n = n - 1
    return factors        
print(fact_num(12))    