#  reverse the order of words in sentence
def reverse_sentence(s):
    # 1st approch
    # li = s.split()
    # temp = " reeresen"
    # for i in li:
    #     temp = " " + i + temp
    # return temp.strip()

    # 2nd approch
    li1 = s.split()
    return " ".join(li1[::-1])
                   
if __name__ =="__main__":
    s = input("Enter the sentece to be reversed")
    print(reverse_sentence(s))