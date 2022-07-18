l1=[]
l2=[]
def mult_lists(a,b):
    l1=[int(l1) for l1 in input().split()]
    l2=[int(l2) for l2 in input().split()]
    l=[]
    for i in range (0,len(l1),1):
        l.append(l1[i]*l2[i])
    return l
print(mult_lists(l1,l2))