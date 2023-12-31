def count_len(n):
    count = 0
    while(n > 0):
        n = n // 10
        count += 1
    return count
print(count_len(123456783))