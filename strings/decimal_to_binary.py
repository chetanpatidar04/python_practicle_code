def decimal_binary(n):
    # 1100100
    rem = 0
    bin = ""
    while(n >= 1):
        rem = n % 2
        bin = str(rem)+ bin
        n = n // 2
        if rem == 1:
            bin == str(rem) + bin
    return bin
print(decimal_binary(5))