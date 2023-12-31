# in = aaabbccccddrr o/p = a3b2c4d2r2

s = "aabbccccddrr222ppj"
print(len(s),len)
# 1st approrch
# di= {}
# for i in s:
#     if i not in di.keys():
#         di[i] = s.count(i)
# temp = ""
# for k,v in di.items():
#     temp = temp + str(k) + str(v)
# print(temp)

# 2nd approch
temp = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count +=1         
    else:
        temp = temp + s[i] + str(count)
        count = 1
temp = temp + s[-1] + str(count)
print(temp)
        