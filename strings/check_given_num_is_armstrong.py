def armstron_num(n):
    li = []
    count = 0
    sum = 0
    temp = n
    while(n > 0):
        li.append(n%10)
        count += 1
        n = n // 10
        
    for i in range(count):
        sum = sum + (li[i] ** count)
    if sum == temp:
        return "number is armstrong number"
    return "Not armstrong num"    



print(armstron_num(153))