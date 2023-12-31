def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] < li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li            

if __name__ == "__main__":
    num = int(input("Enter the number "))
    li = []
    for i in range(num):
        ele = input("enter the elements ")
        li.append(int(ele))
    print(bubble_sort(li))