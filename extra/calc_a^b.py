# calculate a^b:
def cal(x,n):
    if n <=0 :
        return 1
    if x == 0 :
        return 0
    return x * cal(x,n-1)        
print(cal(4,5))    

print(4**5)