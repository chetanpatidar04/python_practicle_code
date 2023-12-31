    
def palindrom(num):
    li=[]
    for j in range(num):
        n = j
        res = 0
        rem = 0
        while (n > 0):
            rem = n % 10    
            n = n // 10     
            res = (res * 10) + rem
            print ("res",res)
        if res == j:
            li.append(res)
    return li    
print(palindrom(100))
