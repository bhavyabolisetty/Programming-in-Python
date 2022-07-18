l=[int(j) for j in input().split()]
f=0
g=0
for i in range (0, len(l)-1,1):
    if(l[i]>l[i+1]):
        f+=1
        continue
    elif(l[i]<l[i+1]):
        g+=1
        continue
    else:
        continue
if(f==len(l)-1):
    print("Decreasing")
elif(g==len(l)-1):
    print("Increasing")
else:
    print("Not a monotonic sequence")