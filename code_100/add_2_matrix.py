m1,m2 = [[1,2,3],[3,4,6],[5,6,7]],[[1,2,3],[3,4,6],[5,6,9]]
li = []
for i in range(len(m1)):
    temp = []
    for j in range(len(m1[i])):
        temp.append(m1[i][j]+m2[i][j])
    li.append(temp)
for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j],end= " ")
    print()    