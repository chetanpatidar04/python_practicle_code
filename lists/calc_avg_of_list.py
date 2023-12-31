# calaculate average of list in python
def average(li):
    temp = 0
    for j in li:
        temp = temp + j
    return (temp/len(li))    
        

if __name__=="__main__":
    num = int ( input("Enter the number"))
    li = []
    for i in range(num):
        ele = int(input("enter the number "))
        li.append(ele)
    print(average(li))