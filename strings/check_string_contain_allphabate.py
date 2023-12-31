#  wtp to check a strign have only alphabat
def check_albhabat(s):
    # return s.isalpha()
    for i in s:
         if not (65 <= ord(i) <= 90 or 97 <= ord(i) <= 122):
            return False
    return True   
    
if __name__ == "__main__":
    s = input("enter the number ")
    print(check_albhabat(s))