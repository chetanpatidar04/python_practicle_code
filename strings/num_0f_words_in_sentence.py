def count_words(n):
    temp = 1
    n = n.strip()
    for i in range(len(n)):
        if n[i] == " ":
            temp = temp + 1
    return temp        
print(count_words("this is a count sentence"))