def triangular_number(n):
    li = []
    i = 1
    while(i < n+1):
        j = 1
        sum = 0
        while(j < i):
           sum = sum + j
           j += 1
        li.append(sum)   
        i = i+1
    return li
print(triangular_number(10))