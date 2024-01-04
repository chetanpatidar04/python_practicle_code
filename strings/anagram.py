# check 2 strings are ana gram
def anagram(s,s1):
    if len(s) != len(s1):
        return "Not anagram"
    else:
        for i in range(len(s)):
            if s[i] not in s1 and s.count(s[i]) != s1.count(s[i]):
                return "Not anagram"
    return True            


print(anagram("silent","listsn"))