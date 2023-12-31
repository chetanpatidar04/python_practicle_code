def count_odd_even(n):
    even = 0
    odd = 0
    while n > 0:
        rem = n % 10
        if rem % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10    
    return odd,even

print(count_odd_even(1234645787))