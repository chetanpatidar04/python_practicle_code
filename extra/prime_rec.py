def check (n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            flag = True
            for j in range(2,i-1):
                if i % j == 0 :
                    flag = False
            if flag:
                print(i)
        return True
print(check(19))    