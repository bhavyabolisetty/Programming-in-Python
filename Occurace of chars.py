n=0
chars=[]
for i in range(100):
    n=input()
    chars.append(n)
print(chars)
counts= {}
for i in chars:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print (str(counts))