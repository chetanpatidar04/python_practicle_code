def sum_of_digit(n):
    sum = 0
    while(n>0):
        sum = sum + (n % 10)
        n = n // 10
    return sum    

print(sum_of_digit(12634))    