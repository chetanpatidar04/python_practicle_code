m1,m2 = [[1,2],[3,4]],[[1,2],[3,4]]
1,2   1,2
3,4   3,4
li = []

for i in range(len(m1)):
    temp =[]
    v1 = 0
    v2 = 0
    for j in range(len(m1[i])):
        v1 = m1[i][j]*m2[j][i]
        v2 = v2 + v1
        # continue