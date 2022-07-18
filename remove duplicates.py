s1=input()
def remove_duplicates(string):
    s2=""
    c=0
    for i in s1:
        if s1.index(i)==c:
            s2+=i
        c+=1
    return s2
print(remove_duplicates(s1))