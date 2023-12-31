#   product of all elementd in python
def product_list(li):
    temp = 1
    for i in li:
        temp = temp * i
    return temp
    
if __name__ == "__main__":
    n = int(input("enter the list len"))
    li = []
    for i in range(n):
        ele = int(input("ele" + str ( i+1)))
        li.append(ele)
    print(product_list(li))