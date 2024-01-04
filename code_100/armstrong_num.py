def armstrong_num(a):
    n = a
    li=[]
    while(a > 0):
        rem = a % 10
        a = a // 10
        li.append(rem)
    temp = 0
    for i in range(len(li)):
        temp = temp + ( li[i] ** len(li))
    if temp == n:
        return "armstrong"
    return "not a armstrong"    
if __name__=="__main__":
    a = int(input("enter  number a "))
    print(armstrong_num(a))