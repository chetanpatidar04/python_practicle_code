# WTP to check given string is a valid email address
import re
def validate_email(email):
    valid = re.compile(r'[a-zA-Z][a-zA-Z0-9.]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(valid.match(email))
    

if __name__ == "__main__":
    email = input("Enter a email ")
    print(validate_email(email))