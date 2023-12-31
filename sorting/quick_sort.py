def quick_sort(li):
    li = [4,2,5,7,1,3,6]
    low = 0
    high = len(li)
    if low < high:
        temp = part(li,low,high)
    return li    

def part(li,low,high):
    p = li[low]
    j = high
    i = low + 1
    while True:
        while (i <= j and li[i] <= p):
            i +=1
        while (i <= j and li[j] >= p):
            j -= 1
        if i <= j:
            li[i],li[j]=li[j],li[i]            
        else:
            break
        li[low],li[j] = li[j],li[low]    
    return j
   
    
if __name__ == "__main__":
    num = int(input("enter the number "))
    li= []
    for i in range(num):
        ele = int(input("enter the elements in python "))
        li.append(ele)
    print(quick_sort(li))