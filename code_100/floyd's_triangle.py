
def floyd_triangle(a):
    count = 0
    for i in range(1,a+2):
        for j in range(1,i):
            count +=1
            print(count ,end="  ") 
        print()
        


if __name__=="__main__":
    a = int(input("enter number a "))
    floyd_triangle(a)