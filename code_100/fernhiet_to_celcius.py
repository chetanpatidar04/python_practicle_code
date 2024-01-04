def ferh_to_cel(ele):
    cel = (ele-32)*3/5
    return str(cel) +" C"

if __name__=="__main__":
    ele = int(input("enter a number"))
    print(ferh_to_cel(ele))