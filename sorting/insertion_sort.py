def insertion_sort(li):
    for i in range(len(li)-1):
        while(i >= 0):
            key = i+1
            if li[i] > li[key]:
                li[i],li[key ] = li[key],li[i]                                
            i -= 1
    return li

if __name__ == "__main__":
    num = int(input("enter the number "))
    li= []
    for i in range(num):
        ele = int(input("enter the elements in python "))
        li.append(ele)
    print(insertion_sort(li))