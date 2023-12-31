def largest_ele(li):
    i = 0
    temp = 0
    while(i<=len(li)-2):
        if li[i] > li[i+1]:
            temp = li[i]
        else:
            temp = li[i+1]
        i = i+1
    return temp

        

if __name__ =="__main__":
    num = int(input("enter the number"))
    li =[]
    for j in range(num):
        li.append(int(input("enter element in list")))
    print(largest_ele(li))