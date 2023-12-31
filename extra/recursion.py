# def rec(n):    
#     if n == 0:
#         return n    
#     return n + rec(n-1)
# print(rec(10))

def fibon(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibon(n-1) + fibon(n-2)

for i in range(10):
    print(fibon(i))        


# Fibonacci series using recursion

# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(9))    