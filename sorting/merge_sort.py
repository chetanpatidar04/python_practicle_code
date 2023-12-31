def merge_sort(li):
    if len(li) <= 1:
       return li
    mid = len(li) // 2
    l_half = li[:mid]
    r_half = li[mid:]
    l_half = merge_sort(l_half)
    r_half = merge_sort(r_half)
    return part(l_half,r_half)
    
def part(l_half,r_half):
    new = []
    i = 0
    j = 0    
    while(i < len(l_half) and j < len(r_half)):
        if l_half[i] < r_half[j]:
            new.append(l_half[i])
            i += 1
        else:
            new.append(r_half[i])
            j += 1
    new.extend(l_half[i:])
    new.extend(r_half[j:])
    return new        
    
if __name__ == "__main__":
    num = int(input("enter the number "))
    # li= []
    # for i in range(num):
    #     ele = int(input("enter the elements in python "))
    #     li.append(ele)
    li = [3,1,5,4,7,8,9,4,2]
    print(merge_sort(li))