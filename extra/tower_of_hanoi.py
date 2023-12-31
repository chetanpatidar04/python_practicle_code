# WTP for TOWER OF HANOI USING RECUSSION
def toi(n,source,helper,dest):
    if (n==1):
        print("disk is transfered " + str(n)+ " from " + source +" to " + dest + "_000" )
        return
    toi(n-1,source,dest,helper)
    print("disk is transfered " + str(n)+ " from " + source +" to " + dest )
    toi (n-1,helper,source,dest)
print(toi(2,"S","H","D"))