def perfct_sq(n,li):    
    i = 1
    while(i<=n):
        if n % i == 0 and n // i == i:
            return ("n is a perfect square")                
        i = i+1
    return ("n is not perfect square")
  
print(perfct_sq(9))