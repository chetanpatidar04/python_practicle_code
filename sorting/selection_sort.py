def selection_sort(li):
    for i in range(len(li)-1):
        sm = i
        for j in range(i+1,len(li)):
            if li[j] > li[sm]:
                sm = j
        li[i],li[sm] =li[sm],li[i]        
    return li   

if __name__ == "__main__":
    num = int(input("enter the number "))
    li= []
    for i in range(num):
        ele = int(input("enter the elements in python "))
        li.append(ele)
    print(selection_sort(li))