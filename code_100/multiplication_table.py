def multiple(a):
    for i in range(1,11):
        res = a*i
        temp = f"""{a} X {i} = {res}"""
        print(temp)

if __name__=="__main__":
    a = int(input("enter  number a "))
    multiple(a)