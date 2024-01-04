def prime(a):
    li = []
    if a == 1:
        return [a]
    else:
        for i in range(2,a+1):
            flag = True
            for j in range(2,i):
                if i % j == 0:
                    flag = False
            if flag:
                li.append(i)        
    return li

if __name__=="__main__":
    a = int(input("enter  number a "))
    print(prime(a))