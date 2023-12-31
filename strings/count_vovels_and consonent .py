# WTP to count vowel and consonent
def count_str(s):
    v_di = ["a","e","i","o","u"]
    vowel = 0
    cons = 0
    for i in s:
        if i not in v_di:
            cons +=1
        else:
            vowel += 1    
    return {"consonnet":cons,"vowel":vowel}

if __name__=="__main__":
    s = input(" enter the string ")
    print(count_str(s))