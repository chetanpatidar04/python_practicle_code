# wtp to convert strign to intiger in python
def str_to_int(s):
    # 1sat approch
    if s.isdigit():
        num = int(s)
    return num
    
    
    
if __name__ =="__main__":
    s = input("enter the string ")
    print(str_to_int(s))