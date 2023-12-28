def add_func(my_l):
    res={}
    res1=[]

    for var, i in enumerate(reversed(my_l)):
        if i in res:
            res1.insert(0, '_')
        else:
            res1.insert(0, i)
            res[i] = var
    
    return res1

print(add_func([1,2,3,1,2]))
    