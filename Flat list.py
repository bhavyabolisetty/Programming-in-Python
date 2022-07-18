def flatten_list():
    l=[1,2,[3,4,5],[7,8]]
    flatlist=[]
    for element in l:
        if type(element) is list:
           for item in element:
               flatlist.append(item)
        else:
            flatlist.append(element)
    return flatlist
print(flatten_list())