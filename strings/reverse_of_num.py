def rev_num(n):
    rev = 0
    rem = 0
    while(n > 0):
        rem = n % 10
        n = n // 10
        rev = (rev * 10 ) + rem
    return rev 
print(rev_num(1234))