def longest_word_in_sentence(s):
    temp = 0
    s =s.strip()
    li = []
    longest_word  = 0
    for i in range(len(s)):
        if s[i] != " " and len(s)-1 > i:
            temp += 1
        elif len(s)-1 == i:
            temp = temp + 1
            if longest_word < temp:
                longest_word,temp = temp,longest_word
            temp = 0    
        else:
            if longest_word < temp:
                longest_word,temp = temp,longest_word
            temp = 0
    return longest_word

print(longest_word_in_sentence("this is a sentence"))